package usermanager

import (
	"database/sql"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"

	"github.com/raksul/gofactor/database"
	"github.com/raksul/gofactor/logger"
	"golang.org/x/crypto/bcrypt"
	"gopkg.in/go-playground/validator.v9"
)

//User it holds data structure of UserData
type User struct {
	ID        int          `json:"id"`
	Email     string       `json:"email" validate:"omitempty,email,max=20"`
	Name      string       `json:"name" validate:"omitempty,min=2,max=20"`
	Password  string       `json:"password" validate:"omitempty,min=8,max=20"`
	CreatedAt sql.NullTime `json:"createdAt"`
	UpdatedAt sql.NullTime `json:"updatedAt"`
}

//getHashedPassword perform bcrypt algo on password
func getHashedPassword(password string) ([]byte, error) {
	encryptedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.MinCost)
	if err != nil {
		logger.Ctx.Errorf("Error while hashing password:%s ", err.Error())
		return nil, err
	}
	return encryptedPassword, nil
}

//parseAndValidateReq It will read http.Request, unmarshall to struct and validate
func parseAndValidateReq(req *http.Request) (*User, error) {
	buf := make([]byte, req.ContentLength)
	_, err := io.ReadFull(req.Body, buf)
	if err != nil {
		return nil, err
	}
	payload := User{}
	err = json.Unmarshal(buf, &payload)
	if err != nil {
		return nil, err
	}
	err = validator.New().Struct(payload)
	if err != nil {
		return nil, err
	}
	return &payload, nil
}

//BuildPatchQuery take data for http.Request and create PATCH/UPDATE query for SQL
func BuildPatchQuery(req *http.Request, id int64) (string, []interface{}, error) {
	var args []interface{}
	queryStr := ""
	payload, err := parseAndValidateReq(req)
	if err != nil {
		return "", args, err
	}

	if payload.Email != "" {
		args = append(args, payload.Email)
		queryStr = queryStr + "email = ?,"
	}
	if payload.Name != "" {
		args = append(args, payload.Name)
		queryStr = queryStr + "name = ?,"
	}
	if payload.Password != "" {
		queryStr = queryStr + "password = ?,"
		var encryptedPassword []byte
		encryptedPassword, _ = getHashedPassword(payload.Password)
		args = append(args, encryptedPassword)
	}

	if len(args) == 0 {
		return "", args, errors.New("None of the item in email/username/password preset")
	}
	args = append(args, id)
	queryStr = "UPDATE gofactor.users SET " + queryStr[:len(queryStr)-1] + " WHERE id = ?"
	logger.Ctx.Debugf("QueryStr:%s", queryStr)
	return queryStr, args, nil
}

//BuildInsertQuery take data for http.Request and create INSERT query for SQL
func BuildInsertQuery(req *http.Request) (string, []interface{}, error) {
	payload, err := parseAndValidateReq(req)
	if err != nil {
		return "", nil, err
	}
	if payload.Email == "" || payload.Name == "" || payload.Password == "" {
		return "", nil, fmt.Errorf("Either Email=[%s], Name=[%s] or Password=[%s] is empty", payload.Email, payload.Name, payload.Password)
	}
	encryptedPassword, err := getHashedPassword(payload.Password)
	if err != nil {
		return "", nil, err
	}
	var args []interface{}
	args = append(args, payload.Email)
	args = append(args, payload.Name)
	args = append(args, encryptedPassword)
	return "INSERT INTO gofactor.users SET email = ?, name = ?, password = ?", args, nil

}

//GetUserData it get data from SQL DB for the given ID
func GetUserData(id int64) ([]byte, error) {
	payload := User{}
	logger.Ctx.Debugf("Fetching user: %d", id)
	payload.ID = int(id)
	err := database.ExecuteSelectCommand("SELECT * FROM gofactor.users WHERE id = ?",
		id, &payload.ID, &payload.Email, &payload.Name, &payload.Password, &payload.CreatedAt, &payload.UpdatedAt)
	if err != nil {
		return nil, err
	}
	return json.Marshal(payload)
}
