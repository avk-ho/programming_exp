package main

import (
	"fmt"
)

type Result struct {
	str string
	idx int
}

func MultiplyStrings(str string, factor uint, idx int, ch chan Result) {
	var multiplied_str string

	var i uint = 0
	for i < factor {
		multiplied_str += str
		i++
	}
	result := Result{multiplied_str, idx}
	ch <- result
}

func MultiplyStringsConcurrently(strings []string, factor uint) []string {
	multiplied_strings := make([]string, len(strings))

	ch := make(chan Result)

	for idx, str := range strings {
		go MultiplyStrings(str, factor, idx, ch)
		// multiplied_strings = append(multiplied_strings, <-ch) // cheating ?
	}

	// fmt.Println(len(multiplied_strings))
	i := 0
	for i < len(strings) {
		result := <-ch
		multiplied_strings[result.idx] = result.str
		i++
	}

	return multiplied_strings
}

func main() {
	arr := []string{}
	arr = append(arr, "hello")
	fmt.Println(arr)
}