package httphandler

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/raksul/gofactor/logger"
	"github.com/stretchr/testify/assert"
)

//TestRoot "/" PATH
func TestRoot(t *testing.T) {
	logger.InitLogger()

	httpHandler := HTTPHandler{}
	r, _ := http.NewRequest("GET", "DUMMY", nil)
	w := httptest.NewRecorder()
	httpHandler.root(w, r)
	resp := w.Result()
	assert.Equal(t, 200, resp.StatusCode, "expected 200 status code")
}

//TestLatestReview "/latset-revies" PATH
func TestLatestReview(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}
	logger.InitLogger()
	fmt.Println("Testing")

	httpHandler := HTTPHandler{}

	r, _ := http.NewRequest("GET", "DUMMY", nil)
	w := httptest.NewRecorder()
	httpHandler.latestReviews(w, r)
	resp := w.Result()
	assert.Equal(t, 200, resp.StatusCode, "expected 200 status code")
}

//TestUserGetWithoutID "/user/{id}" PATH without ID
func TestUserGetWithoutID(t *testing.T) {
	logger.InitLogger()
	fmt.Println("Testing")

	httpHandler := HTTPHandler{}

	r, _ := http.NewRequest("GET", "DUMMY", nil)
	w := httptest.NewRecorder()
	httpHandler.getUser(w, r)
	resp := w.Result()
	// StatusBadRequest as ID is not provided
	assert.Equal(t, 400, resp.StatusCode, "expected 200 status code")
}

// func TestUserGetWithID(t *testing.T) {
// 	logger.InitLogger()
// 	fmt.Println("Testing")

// 	usermanager.GetUserData = func(id int) int { return 1 }

// 	httpHandler := HTTPHandler{}

// 	r, _ := http.NewRequest("GET", "DUMMY", nil)
// 	r = mux.SetURLVars(r, map[string]string{"id": "1"})
// 	w := httptest.NewRecorder()
// 	httpHandler.getUser(w, r)
// 	resp := w.Result()
// 	// StatusBadRequest as ID is not provided
// 	assert.Equal(t, 400, resp.StatusCode, "expected 200 status code")
// }
