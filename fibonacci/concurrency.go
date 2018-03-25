package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func fibonacci(num int64) int64 {
	if num <= 2 {
		return 1
	}
	return fibonacci(num-1) + fibonacci(num-2)
}

func task(wg *sync.WaitGroup, num int64) {
	defer wg.Done()
	fmt.Println(num, " : ", fibonacci(num))
}

func main() {

	runtime.GOMAXPROCS(2)
	fmt.Println("Using ", 2, " logical cores")

	var wg sync.WaitGroup
	wg.Add(2)

	start := time.Now()

	go task(&wg, 50)
	go task(&wg, 50)

	wg.Wait()
	fmt.Print("\nTime : ")
	fmt.Print(time.Since(start).Seconds(), "seconds")
}
