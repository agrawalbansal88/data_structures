package main

import (
	_ "github.com/go-sql-driver/mysql"
	"github.com/raksul/gofactor/database"
	"github.com/raksul/gofactor/httphandler"
	"github.com/raksul/gofactor/logger"
)

func main() {
	logger.InitLogger()
	//Init DB context
	err := database.GetDbCtx().InitCtx()
	if err != nil {
		logger.Ctx.Errorf("Error while Init DbCtx error:%s", err.Error())
		return
	}
	defer database.CloseConnection()

	//Register routers
	err = httphandler.RegisterHTTPHander()
	if err != nil {
		logger.Ctx.Errorf("Error while Starting HTTP Server :%s", err.Error())
	}
}
