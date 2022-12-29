package main

import (
	"fmt"
	"errors"
	"strconv"
)

func doPanic() {
	// panic("fail")
}

func handlePanic() {
	r := recover()
	if r != nil {
		fmt.Println(r)
	}
}

func divide(a int, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	// fmt.Println("Hello world!")
	// defer fmt.Println("defer")
	// panic("fail")
	// fmt.Println("goodbye")

	defer handlePanic()
	fmt.Println("start")
	doPanic()
	fmt.Println("end")

	result, err := divide(1, 0)
	fmt.Println(result, err)

}

func SumNumericStrings(strings []string) (int, error) {
	// Write your code here
	sum := 0
	for _, str := range strings {
		if len(str) >= 20 {
			return 0, errors.New("string longer than 19 characters")
		}
		value, err := strconv.Atoi(str)

		if err != nil {
			return 0, errors.New("string contains non numerical character")
		}

		sum += value
	} 
	
	return sum, nil
}
