package httphandler

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"strconv"
	"time"

	"github.com/raksul/gofactor/logger"
	"github.com/raksul/gofactor/usermanager"

	"github.com/gorilla/mux"
	"github.com/raksul/gofactor/database"
)

//HTTPHandler hold cached data for Latest review call
type HTTPHandler struct {
	lastSynced time.Time
	cachedData bytes.Buffer
}

//RegisterHTTPHander register handlers and start listing on 8090 port
func RegisterHTTPHander() error {
	httpHandler := HTTPHandler{}
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", httpHandler.root).Methods("GET")
	router.HandleFunc("/user", httpHandler.postUser).Methods("POST")
	router.HandleFunc("/user/{id}", httpHandler.getUser).Methods("GET")
	router.HandleFunc("/user/{id}", httpHandler.patchUser).Methods("PATCH")
	router.HandleFunc("/latest-reviews", httpHandler.latestReviews).Methods("GET")
	logger.Ctx.Infof("Server listening on port 8090")
	return http.ListenAndServe(":8090", router)
}

//getUser handles GET on /user
func (httpHandler *HTTPHandler) getUser(w http.ResponseWriter, req *http.Request) {
	id, err := strconv.ParseInt(mux.Vars(req)["id"], 10, 32)
	if err != nil {
		logger.Ctx.Errorf("Error while parsing ID: %s", err.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	fillSuccResponse(w, id)
}

//postUser handles POST on /user
func (httpHandler *HTTPHandler) postUser(w http.ResponseWriter, req *http.Request) {
	queryStr, args, err := usermanager.BuildInsertQuery(req)
	if err != nil {
		logger.Ctx.Errorf("buildInsertQuery failed: %s", err.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	var lastID int64
	lastID, err = database.ExecuteInsertCommand(queryStr, args...)
	if err != nil {
		logger.Ctx.Errorf("DB INSERT FAILED: %s", err.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	fillSuccResponse(w, lastID)
}

//patchUser handles PATCH on /user
func (httpHandler *HTTPHandler) patchUser(w http.ResponseWriter, req *http.Request) {
	id, err := strconv.ParseInt(mux.Vars(req)["id"], 10, 32)
	if err != nil {
		logger.Ctx.Errorf("Error while parsing ID:%s", err.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	queryStr, args, err := usermanager.BuildPatchQuery(req, id)
	if err != nil {
		logger.Ctx.Errorf("None of the attribute from name/password/email is present in request: %s", err.Error())
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	if err = database.ExecuteUpdateCommand(queryStr, args, id); err != nil {
		logger.Ctx.Errorf("Error while executing query: %s", err.Error())
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	fillSuccResponse(w, id)
}

//latestReviews handles GET on /latest-reviews
func (httpHandler *HTTPHandler) latestReviews(w http.ResponseWriter, req *http.Request) {
	if httpHandler.lastSynced.IsZero() || time.Since(httpHandler.lastSynced).Hours() >= 1 {
		logger.Ctx.Debugf("Fetching latest reviews ..")
		resp, err := http.Get("https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=&api-key=1ODRGmfb2AOQGeKCuwZXqik6LCfrSIHh")
		if err != nil {
			logger.Ctx.Errorf("Error while getting HTTP response:%s", err.Error())
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
		defer resp.Body.Close()
		logger.Ctx.Debugf("Response status:%d", resp.Status)
		rsp := io.MultiWriter(w, &httpHandler.cachedData)
		io.Copy(rsp, resp.Body)
		httpHandler.lastSynced = time.Now()

	} else {
		logger.Ctx.Debugf("Getting latest reviews from cache")
		w.Write(httpHandler.cachedData.Bytes())
	}
}

//root handles GET on /
func (httpHandler *HTTPHandler) root(w http.ResponseWriter, req *http.Request) {
	logger.Ctx.Debugf("Received GET request on root")
	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	fmt.Fprintf(w, `{"Message":"hello, it's %s"}`, time.Now())
}

//fillSuccResponse fills response for HTTP USER requests
func fillSuccResponse(w http.ResponseWriter, id int64) {
	userJSON, err := usermanager.GetUserData(id)
	if err == nil {
		logger.Ctx.Debugf("Sending SUCCESS response for ID: %d", id)
		w.WriteHeader(http.StatusOK)
		w.Write(userJSON)
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	}
}
