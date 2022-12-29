package main

import "fmt"

func test(a int, b int) (x int, y int) {
	x = a
	y = b
	return
}

func sumInts(nums ...int) int {
	sum := 0
	for _, val := range nums {
		sum += val
	}
	return sum
}

func returnFunc(x int) func(int) int {
	return func(y int) int {
		return x + y
	}
}

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func callFunc(callable func(string) string, arg string) {
	result := callable(arg)
	fmt.Println(result)
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	sum := sumInts(nums...)
	fmt.Println(sum)

	fn := returnFunc(100)
	value := fn(50)
	fmt.Println(value)

	pos := adder()
	neg := adder()

	for i := 0; i < 10; i++ {
		fmt.Println(pos(i), neg(-2*i))
	}

	myFunc := func(str string) string {
		return str + "hello"
	}
	callFunc(myFunc, "world")
}


func AddN(n int) func(int) int {
    return func(num int) int {
        return n + num
    }
}

func FilterStrings(strings []string, filter func(str string) bool) []string {
    filtered_str := []string{}

    for _, elem := range strings {
        if filter(elem) {
            filtered_str = append(filtered_str, elem)
        }
    }

    return filtered_str
}

type Employee struct {
	salary float64
	bonus  float64
}

func GetEmployeeWages(employees []Employee) (sum_salaries float64, sum_bonuses float64) {
	for _, e := range employees {
		sum_salaries += e.salary
		sum_bonuses += e.bonus
	}
	return
}