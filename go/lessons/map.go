package main

import "fmt"

func main() {
	n := 100
	divisibleMap := make(map[int]uint)

	for num := 1; num <= n; num++ {
		for d := 1; d <= 5; d++ {
			if num % d == 0 {
				divisibleMap[d]++
			}
		}
	}
	fmt.Println(divisibleMap)
}

func CharacterFrequency(sentence string) map[rune]int {
	// Write your code here.
	mp := make(map[rune]int)

	for i := 0; i < int(len(sentence)); i++ {
		mp[rune(sentence[i])]++
	}

	return mp
}

func MergeMaps(heights map[int][]string, ages map[int][]string) map[string][]int {
	// Write your code here.
	mp := make(map[string][]int)

	for height, names := range heights {
		for _, name := range names {
			mp[name] = []int{height}
		}
	}

	for age, names := range ages {
		for _, name := range names {
			mp[name] = append(mp[name], age)
		}
	}

	return mp
}