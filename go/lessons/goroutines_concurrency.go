package main

import (
	"fmt"
	"sync"
	"time"
)

func run1() {
	time.Sleep(1 * time.Second)
	fmt.Println("run1")
}

func run2() {
	time.Sleep(2 * time.Second)
	fmt.Println("run2")
}

func run3() {
	time.Sleep(3 * time.Second)
	fmt.Println("run3")
}

func add(a int, b int, rv chan int) {
	time.Sleep(1 * time.Second)
	rv <- a + b
}

type Counter struct {
	value int
	mutex sync.Mutex
}

func increment(counter *Counter, wg *sync.WaitGroup) {
	counter.mutex.Lock()
	defer counter.mutex.Unlock()
	counter.value = counter.value + 1
	fmt.Println(counter.value)
	wg.Done()
}

func main() {
	// go run1()
	// go run2()
	// go run3()
	// time.Sleep(4 * time.Second)
	// fmt.Println("done")

	returnChan := make(chan int)
	go add(1, 2, returnChan)
	go add(3, 4, returnChan)
	go add(5, 6, returnChan)
	go add(7, 8, returnChan)
	rv := <-returnChan
	fmt.Println(rv)
	rv = <-returnChan
	fmt.Println(rv)
	rv = <-returnChan
	fmt.Println(rv)
	rv = <-returnChan
	fmt.Println(rv)

	chan1 := make(chan int)
	chan2 := make(chan int)
	go add(5, 5, chan1)
	go add(10, 10, chan2)
	// rv1 := <-chan1
	// rv2 := <-chan2
	// fmt.Println(rv1, rv2)
	for i := 0; i < 2; i++ {
		select {
		case rv1 := <-chan1:
			fmt.Println(rv1)
		case rv2 := <-chan2:
			fmt.Println(rv2)
		}
	}

	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	fmt.Println(<-ch)
	fmt.Println(<-ch)

	counter := Counter{value:0}
	wg := sync.WaitGroup{}
	wg.Add(100)
	// cha := make(chan bool)
	for i := 0; i < 100; i++ {
		go increment(&counter, &wg)
	}

	// make sure we get 100 executions of the loop, replaced by wg
	// results := 0
	// for results < 100 {
	// 	<-cha
	// 	results++
	// }

	wg.Wait()
}

func SumPartialRange(start uint, end uint, result chan<- uint) {
	var sum uint = 0
	for i := start; i <= end; i++ {
		sum = sum + i
	}

	result <- sum

}

func SumToN(n uint) uint {
	// Write your code here.
	half1 := make(chan uint)
	half2 := make(chan uint)
	go SumPartialRange(1, n/2, half1)
	go SumPartialRange((n/2 + 1), n, half2)
	sum1 := <- half1
	sum2 := <- half2

	return sum1 + sum2
}

//
type MappedSums struct {
	mutex sync.Mutex
	sums  map[string]uint
}

func (m *MappedSums) Increment(key string, value uint) {
	m.mutex.Lock()
	defer m.mutex.Unlock()
	_, ok := m.sums[key]
	if !ok {
		m.sums[key] = value
	} else {
		m.sums[key] += value
	}
}

func CreateMappedSums(keys []string, sumTo []uint) map[string]uint {
	mappedSums := MappedSums{sums: make(map[string]uint)}
	var wg sync.WaitGroup

	doIncrement := func(key string, n uint) {
		for i := uint(1); i <= n; i++ {
			mappedSums.Increment(key, i)
		}
		wg.Done()
	}

	wg.Add(len(keys))

	for i, key := range keys {
		go doIncrement(key, sumTo[i])
	}

	wg.Wait()

	return mappedSums.sums
}

//
func CollectGoRoutines(goRoutines []func(chan<- string)) []string {
	results := []string{}

	ch := make(chan string, len(goRoutines))
	for _, r := range goRoutines {
		go r(ch)
	}

	for len(results) < len(goRoutines) {
		results = append(results, <-ch)
	}

	return results
}