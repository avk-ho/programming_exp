// https://www.programmingexpert.io/programming-with-go/assessment/1

package main

import "fmt"

func KeepLongestAndShortestWord(wordSlices *[][]string) {
	for i, slice := range *wordSlices {
		if len(slice) > 2 {
			longest_idx := 0
			shortest_idx := 0

			for i, word := range slice {
				word_len := len(word)
				if word_len > len(slice[longest_idx]) {
					longest_idx = i
				}
				if word_len < len(slice[shortest_idx]) {
					shortest_idx = i
				}
			}

			longest_word := slice[longest_idx]
			shortest_word := slice[shortest_idx]
			if longest_idx < shortest_idx {
				slice[0] = longest_word
				slice[1] = shortest_word
				// slice = slice[:2]
			} else if longest_idx > shortest_idx {
				slice[0] = shortest_word
				slice[1] = longest_word
				// slice = slice[:2]
			}
			(*wordSlices)[i] = slice[:2]
			// fmt.Println(slice)

		}
	}
}

// [["best", "course", "yes"], ["hello"], []] // [["course", "yes"], ["hello"], []]

func main() {
	slice := []int{1, 2, 3}
	slice = slice[:2]
	fmt.Println(slice)

	words := &[][]string{{"best", "course", "yes"}, {"hello"}, {}}
	KeepLongestAndShortestWord(words)
	fmt.Println(words)
}