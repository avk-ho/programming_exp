package main

import ("fmt"
"math"
"strconv"
)

func main() {
	a := 1
	b := 2
	c := a + b
	fmt.Println(c)

	// x := math.Max(5, 10)
	// y := math.Min(5, 10)
	z := math.Floor(25.6)
	fmt.Println(z)

	str := "1234"
	x, err := strconv.Atoi(str)
	fmt.Println(x, err)

}