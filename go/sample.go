package main

import (
	"fmt"
	"time"
)

func main() {

	c1 := make(chan string, 1)

	// Run your long running function in it's own goroutine and pass back it's
	// response into our channel.
	go func() {
		text := LongRunningProcess()
		c1 <- text
	}()

	// Listen on our channel AND a timeout channel - which ever happens first.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("out of time :(")
	}
	fmt.Println("exit from select")
	time.Sleep(5 * time.Second)
	fmt.Println("exit from main")

}

func LongRunningProcess() string {
	fmt.Println("Sleep start")
	time.Sleep(5 * time.Second)
	fmt.Println("Sleep end")
	return "My golangcode.com example is finished :)"
}
