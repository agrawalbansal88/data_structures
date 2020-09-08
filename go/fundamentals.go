package main

import "fmt"

func variadic(items ...int) int {
	ret := 0
	for _, i := range items {
		ret = ret + i
	}
	return ret
}

func slices() {
	//slices
	slice := make([]int, 10, 20)
	slice[2] = 2
	fmt.Println("BEFORE slice is ", slice)
	new_slice := make([]int, 4)
	copy(slice[1:5], new_slice)
	new_slice[3] = 11
	slice[3] = 3
	fmt.Println("AFTER slice is ", slice)
	fmt.Println("new_slice", new_slice)

	slice1 := []int{1, 2, 3}
	slice2 := make([]int, 2)
	slice2[1] = 22
	slice2 = append(slice2, slice1...)
	fmt.Println("ADDING TO SLICE", slice2)
}

func maps() {
	type ankur struct {
		x string
		y int
		//z []int
	}

	map1 := make(map[int]string)
	map1[1] = "one"
	fmt.Println("map1", map1)

	map2 := map[int]string{1: "one", 2: "tow"}
	fmt.Println("map1", map2)

	customMap := make(map[ankur]string)
	key := ankur{x: "ABC", y: 20}
	customMap[key] = "value"
	fmt.Println("Custom map, %v", customMap)
}

type inter interface {
	InterFunc(string) string
	//InterFunc1(string) int
}

type mystruct struct {
	xx string
}

func (f *mystruct) InterFunc(string) string {
	return "abc"
}

func CheckInter(in inter) {
	return
}

func interfacess() {

	str := mystruct{xx: "Ankir"}
	str.InterFunc("PAP")
	CheckInter(&str)
}
func main() {

	//variadic function
	//ret := variadic(1, 2, 3, 4)
	//fmt.Println(" variadic Retval ", ret)
	//slices()
	//maps()
	interfacess()

}
