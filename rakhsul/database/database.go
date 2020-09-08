package database

import (
	"database/sql"
	"errors"
	"flag"
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/raksul/gofactor/logger"
)

// DatabaseCtx holds DB connectoin and DSN
type DatabaseCtx struct {
	db  *sql.DB
	dsn string
}

var dbCtx *DatabaseCtx

//GetDbCtx will check and init context
func GetDbCtx() *DatabaseCtx {
	if dbCtx == nil {
		dbCtx = new(DatabaseCtx)
	}
	return dbCtx
}

//InitCtx get ENV variables, check reset DB and INIT DB connection
func (dbCtx *DatabaseCtx) InitCtx() error {
	// not storing username and password in config struct as it is not used in future
	username := os.Getenv("SQL_DB_USERNAME")
	password := os.Getenv("SQL_DB_PASSWORD")
	if username == "" || password == "" {
		return errors.New("Either username or password ENV not set")
	}

	ipAddress := os.Getenv("SQL_DB_IP_ADDRESS")
	if ipAddress == "" {
		// this bypass is added for local testing, can be removed as well
		ipAddress = "localhost"
	}

	dbCtx.dsn = fmt.Sprintf("%s:%s@tcp(%s:3306)/gofactor?timeout=90s&charset=utf8mb4&collation=utf8mb4_unicode_ci&parseTime=true", username, password, ipAddress)
	logger.Ctx.Infof("DSN is : %s", dbCtx.dsn)

	//check if "init-db" set
	if isDbInit, err := dbCtx.CheckFlagAndInitDB(); isDbInit {
		if err != nil {
			logger.Ctx.Errorf("Error while CheckFlagAndInitDB:%s", err.Error())
		}
		logger.Ctx.Infof("Exiting")
		os.Exit(0)
	}
	if err := dbCtx.InitConnection(); err != nil {
		logger.Ctx.Errorf("Error while InitConnection:%s", err.Error())
	}
	return nil
}

//CheckFlagAndInitDB check "init-db" and if it is present then RESET DB
func (dbCtx *DatabaseCtx) CheckFlagAndInitDB() (bool, error) {
	initDB := flag.Bool("init-db", false, "initialize db")
	flag.Parse()

	var err error

	if *initDB {
		logger.Ctx.Infof("Initializing database ..")
		dbCtx.db, err = sql.Open("mysql", strings.Replace(dbCtx.dsn, "/gofactor", "/", 1))
		if err != nil {
			return true, err
		}
		defer dbCtx.db.Close()

		_, err = dbCtx.db.Exec("DROP DATABASE IF EXISTS gofactor")
		if err != nil {
			return true, err
		}
		_, err = dbCtx.db.Exec("CREATE DATABASE gofactor")
		if err != nil {
			return true, err
		}
		_, err = dbCtx.db.Exec(`
		CREATE TABLE gofactor.users (
			id INT AUTO_INCREMENT PRIMARY KEY,
			email VARCHAR(20) NOT NULL UNIQUE KEY,
			name VARCHAR(20) NOT NULL,
			password BINARY(60) NOT NULL,
			created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
			updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
		)`)
		if err != nil {
			return true, err
		}
		logger.Ctx.Infof("Done..")
		return true, nil
	}
	return false, nil
}

//InitConnection Open DB connection and test connection using ping
func (dbCtx *DatabaseCtx) InitConnection() error {
	var err error
	logger.Ctx.Infof("Connecting to database ..")
	dbCtx.db, err = sql.Open("mysql", dbCtx.dsn)
	if err != nil {
		return err
	}
	time.Sleep(5 * time.Second)
	logger.Ctx.Infof("Pinging database ..")
	err = dbCtx.db.Ping()
	if err != nil {
		return err
	}
	return nil
}

//ExecuteUpdateCommand execute UPDATE SQL command
func ExecuteUpdateCommand(queryStr string, args []interface{}, id int64) error {
	r, err := dbCtx.db.Exec(queryStr, args...)
	if err != nil {
		return err
	}
	rows, _ := r.RowsAffected()
	logger.Ctx.Debugf("Updated user: %d (%d rows)", id, rows)
	return nil
}

//ExecuteInsertCommand execute INSERT DB command
func ExecuteInsertCommand(queryStr string, args ...interface{}) (int64, error) {
	r, err := dbCtx.db.Exec(queryStr, args...)
	if err != nil {
		return 0, err
	}
	lastID, _ := r.LastInsertId()
	logger.Ctx.Debugf("Created new user: %d", lastID)
	return lastID, nil
}

//ExecuteSelectCommand execute SELECT command
func ExecuteSelectCommand(queryStr string, id int64, args ...interface{}) error {
	r, err := dbCtx.db.Query(queryStr, id)
	if err != nil {
		return err
	}
	defer r.Close()
	if r.Next() {
		err = r.Scan(args...)
		if err != nil {
			return err
		}
	} else {
		return fmt.Errorf("Entry not found for ID:%d ", id)
	}
	return nil
}

//CloseConnection closes connection
func CloseConnection() {
	logger.Ctx.Debugf("Closing connection")
	dbCtx.db.Close()
}

//GetDb export DB connection to other packages
func GetDb() *sql.DB {
	return GetDbCtx().db
}
