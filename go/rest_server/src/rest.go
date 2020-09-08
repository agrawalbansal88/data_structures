package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

type Article struct {
	Title   string `json:"Title"`
	Content string `json:"NewContent"`
}

type Articles []Article

func homepage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome to Ankur Page")
}

func getData(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Giveing data\n")
	fmt.Fprint(w, "Data:\n")
	articals := Articles{
		Article{Title: "ABVC", Content: "Very fresh content"},
	}
	json.NewEncoder(w).Encode(articals)
}
func postData(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "POST CALLED")
}

func handleRequests() {
	myRouter := mux.NewRouter().StrictSlash(true)
	myRouter.HandleFunc("/", homepage).Methods("GET")
	myRouter.HandleFunc("/data", getData).Methods("GET")
	myRouter.HandleFunc("/data", postData).Methods("POST")
	http.ListenAndServe(":8081", myRouter)
}

func main() {
	fmt.Println("Application to start web server")
	handleRequests()
	return
}
