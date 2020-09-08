package new_package

import "fmt"

type User2 struct {
	ID   int
	Name string
}

var (
	users  []*User2
	nextId = 1
)

func new_pack_func1() {

	fmt.Println("New package")
}
