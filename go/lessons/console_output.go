package main

import "fmt"

func main() {
	x := 1
	fmt.Println("hello\n", x)
	fmt.Println("hello", 2, 2.45)

	a := 27.2
	b := true
	c := "hello"
	output := fmt.Sprintf("%%%v:%v/%s", a, b, c)
	fmt.Println(output)
}