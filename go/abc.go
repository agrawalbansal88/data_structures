package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	//part1()
	part2()
}

type intf interface {
	aa() error
	cc() error
}

type Ankur struct {
	x int
	y string
}

func (ank *Ankur) aa() error {
	ank.x = 11
	return nil

}
func (ank *Ankur) bb() {

}

func (ank *Ankur) cc() error {
	return nil

}
func intf_func(in intf) {
	in.aa()
}

func part2() {
	ank := &Ankur{x: 10, y: "B"}
	ank.aa()

	fmt.Println("ankur", ank)
	intf_func(ank)

	xx := make([]int, 0, 5)
	fmt.Println("SLIEVEEE", xx)
}

func part1() {
	fmt.Println("Starting")

	abc := []int{10, 20}
	var xyz []int
	xyz = make([]int, 0)
	xyz = append(xyz, 2)
	fmt.Println("abc", abc, xyz)

	for index, value := range abc {
		fmt.Println("abc ", index, value)
	}

	mapabc := make(map[int]int)

	mapabc[11] = 111
	mapabc[22] = 222
	mapabc[33] = 333
	fmt.Println("mapabc", mapabc)

	for key, value := range mapabc {
		fmt.Println("mapabc", key, value)
	}

	value, ok := mapabc[33]
	fmt.Println("checking ", value, ok)

	chann := make(chan int, 10)
	wg := sync.WaitGroup{}
	wg.Add(1)
	go checkChan(chann, &wg)

	select {
	case val := <-chann:
		fmt.Println("receievd value ", val)
	case <-time.After(time.Second * 2):
		fmt.Println("Timeout")
	}
	fmt.Println("before wait")
	wg.Wait()
	fmt.Println("Exiting")

}
func checkChan(ch chan int, wg *sync.WaitGroup) {
	time.Sleep(3 * time.Second)
	ch <- 11
	wg.Done()
	fmt.Println("goroutine done")
}
