package main

import (
	"fmt"
	"sync"
)

//UNBUFFERED CHANNELS
func UNbuffered_channels() {
	wg := &sync.WaitGroup{}
	ch := make(chan int)

	wg.Add(2)
	go func(ch chan int, wg *sync.WaitGroup) {
		fmt.Println(<-ch)
		wg.Done()
	}(ch, wg)
	go func(ch chan int, wg *sync.WaitGroup) {
		ch <- 42
		wg.Done()
	}(ch, wg)

	wg.Wait()
}

func buffered_channels() {
	wg := &sync.WaitGroup{}
	ch := make(chan int, 1)

	wg.Add(2)
	go func(ch chan int, wg *sync.WaitGroup) {
		fmt.Println(<-ch)
		wg.Done()
	}(ch, wg)
	go func(ch chan int, wg *sync.WaitGroup) {
		ch <- 42
		ch <- 27
		wg.Done()
	}(ch, wg)

	wg.Wait()
}



func chaneel_type() {
	wg := &sync.WaitGroup{}
	ch := make(chan int, 1)

	wg.Add(2)
	//receiver
	go func(ch <-chan int, wg *sync.WaitGroup) {
		fmt.Println(<-ch)
		wg.Done()
	}(ch, wg)

	//sender
	go func(ch chan<- int, wg *sync.WaitGroup) {
		ch <- 42
		wg.Done()
	}(ch, wg)

	wg.Wait()
}

func close_channel() {
	wg := &sync.WaitGroup{}
	ch := make(chan int, 1)

	wg.Add(2)
	go func(ch chan int, wg *sync.WaitGroup) {
		fmt.Println(<-ch)
		close(ch)
		fmt.Println(<-ch)
		wg.Done()
	}(ch, wg)
	go func(ch chan int, wg *sync.WaitGroup) {
		ch <- 42
		ch <- 27
		wg.Done()
	}(ch, wg)

	wg.Wait()
}

func close_channel_if_statement() {
	wg := &sync.WaitGroup{}
	ch := make(chan int)

	wg.Add(2)
	go func(ch <-chan int, wg *sync.WaitGroup) {
		if msg, ok := <-ch; ok {
			fmt.Println(msg, ok)
		}
		wg.Done()
	}(ch, wg)
	go func(ch chan<- int, wg *sync.WaitGroup) {
		close(ch)
		wg.Done()
	}(ch, wg)

	wg.Wait()
}

func close_channel_for_statement() {
	wg := &sync.WaitGroup{}
	ch := make(chan int)

	wg.Add(2)
	go func(ch <-chan int, wg *sync.WaitGroup) {
		for i := range ch {
			fmt.Println(i)
		}
		wg.Done()
	}(ch, wg)
	go func(ch chan<- int, wg *sync.WaitGroup) {
		for i := 0; i < 10; i++ {
			ch <- i
		}
		close(ch)
		wg.Done()
	}(ch, wg)

	wg.Wait()
}

func close_channel_select_statement(){
	fmt.Println("from cache")
	// var cache = map[int]Book{}
	// var rnd = rand.New(rand.NewSource(time.Now().UnixNano()))
	
	// func main_dummy() {
	// 	wg := &sync.WaitGroup{}
	// 	m := &sync.RWMutex{}
	// 	cacheCh := make(chan Book)
	// 	dbCh := make(chan Book)
	
	// 	for i := 0; i < 10; i++ {
	// 		id := rnd.Intn(10) + 1
	// 		wg.Add(2)
	// 		go func(id int, wg *sync.WaitGroup, m *sync.RWMutex, ch chan<- Book) {
	// 			if b, ok := queryCache(id, m); ok {
	// 				ch <- b
	// 			}
	// 			wg.Done()
	// 		}(id, wg, m, cacheCh)
	// 		go func(id int, wg *sync.WaitGroup, m *sync.RWMutex, ch chan<- Book) {
	// 			if b, ok := queryDatabase(id); ok {
	// 				m.Lock()
	// 				cache[id] = b
	// 				m.Unlock()
	// 				ch <- b
	// 			}
	// 			wg.Done()
	// 		}(id, wg, m, dbCh)
	
	// 		go func(cacheCh, dbCh <-chan Book) {
	// 			select {
	// 			case b := <-cacheCh:
	// 				fmt.Println("from cache")
	// 				fmt.Println(b)
	// 				<-dbCh
	// 			case b := <-dbCh:
	// 				fmt.Println("from database")
	// 				fmt.Println(b)
	// 			}
	// 		}(cacheCh, dbCh)
	// 		time.Sleep(150 * time.Millisecond)
	// 	}
	// 	wg.Wait()
	// }
	
// }

// func queryCache(id int, m *sync.RWMutex) (Book, bool) {
// 	m.RLock()
// 	b, ok := cache[id]
// 	m.RUnlock()
// 	return b, ok
// }

// func queryDatabase(id int) (Book, bool) {
// 	time.Sleep(100 * time.Millisecond)
// 	for _, b := range books {
// 		if b.ID == id {
// 			return b, true
// 		}
// 	}

// 	return Book{}, false
}

//BUFFERED CHANNELS
func main() {
	buffered_channels()
	UNbuffered_channels()
	chaneel_type()
	close_channel()
	close_channel_if_statement()
	close_channel_for_statement()
	close_channel_select_statement()

}