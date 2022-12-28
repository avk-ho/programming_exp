package main

import "fmt"

func main() {
	// arr := [...]int{1, 2, 3, 4, 5}
	arr2 := [2][2]string{{"hello", "world"}, {"code", "go"}}

	for _, nestedArr := range arr2 {
		for i, str := range nestedArr {
			fmt.Println(i, str)
		}
	}
	test(arr2)
	fmt.Println(arr2)

	arr := [5]int{1, 2, 3, 4, 5}
	// sliceArr := arr[:4]
	// fmt.Println(sliceArr, len(sliceArr), cap(sliceArr)) // [1, 2, 3, 4] 4 5
	// sliceArr = sliceArr[1:]
	// fmt.Println(sliceArr, len(sliceArr), cap(sliceArr)) // [2, 3, 4] 3 4

	sliceArr := arr[1:4]
	fmt.Println(arr, sliceArr)
	sliceArr[0] = 100
	arr[3] = 200
	fmt.Println(arr, sliceArr)

	arr3 := []string{}

	for i := 0; i < 10; i++ {
		arr3 = append(arr3, "hello")
		fmt.Println(arr3, len(arr3), cap(arr3))
	}

	arr4 := make([][]int, 5)
	fmt.Println(arr4, len(arr4), cap(arr4))

	arr5 := []bool{}
	arr6 := []bool{true, false, false}
	arr5 = append(arr5, arr6...)
}

func test(x [2][2]string) {
	x[0][0] = "new string"
}

func NestedSliceSum(numbers [][]int) []int {
	// Write your code here.
	result := []int{}
	for _, nestedArr := range numbers {
		sum := 0
		for _, val := range nestedArr {
			sum = sum + val
		}
		result = append(result, sum)
	}
	return result
}