package main

import (
	"ankur/new_package"
	"fmt"
)

func array() {

	var firstName *string = new(string)
	*firstName = "Baba"
	fmt.Println(*firstName)

	arr := [4]int{1, 2, 5, 6}
	for key, val := range arr {
		fmt.Println(key, val)
	}
}
func slice() {

	slice := []int{0, 1, 2, 3, 4}
	slice = append(slice, 5)
	fmt.Println("PRINTING ARRAY", slice)
	slice = append(slice, 12, 54, 54)
	fmt.Println("PRINTING ARRAY", slice)
	s2 := slice[2:]
	s3 := slice[:3]
	s4 := slice[2:3]
	fmt.Println(s2, s3, s4)
}

func mapp() {
	m := map[string]int{"foo": 42, "bar": 11}
	fmt.Println(m)
	fmt.Println(m["foo"])
	delete(m, "bar")
	fmt.Println(m)
}
func structs() {
	type user struct {
		ID    int
		First string
	}

	var u user
	u.ID = 123
	u.First = "SDE"
	fmt.Println(u)

	u2 := user{ID: 11, First: "singe"}
	fmt.Println(u2)
}

func package_test() {
	u := new_package.User2{ID: 32, Name: "ANKUR"}
	fmt.Println(u)
}
func main() {
	fmt.Println("Ankur\n")
	//array()
	//slice()
	//mapp()
	//structs()
	package_test()

	return
}
