package main

import "fmt"


func DetectMagicSquare(square [][]int) bool {
	var is_magic_square bool = true
	var magic_num int = 0
	square_len := len(square)
	i := 0
	j := 0
	
	// checking all rows
	sum := 0
	for i < square_len && is_magic_square {
		sum += square[i][j]
		j++
		if j == square_len {
			if i == 0 {
				magic_num = sum
				// fmt.Println(magic_num)
			}
			i++
			j = 0
			if sum != magic_num {
				is_magic_square = false
			}
			sum = 0
		}
	}
	// fmt.Println(magic_num)
	// fmt.Println(is_magic_square)

	// checking all columns
	i = 0
	j = 0
	for j < square_len && is_magic_square {
		sum += square[i][j]
		i++
		if i == square_len {
			j++
			i = 0
			if sum != magic_num {
				is_magic_square = false
			}
			// fmt.Println(sum)
			sum = 0
		}
		
	}

	// checking diagonal top-left, bottom-right
	i = 0
	j = 0
	for i < square_len && is_magic_square {
		sum += square[i][i]
		i++
	}
	if sum != magic_num {
		is_magic_square = false
	}
	// fmt.Println(sum)

	// checking diagonal top-right, bottom-left
	i = 0
	j = square_len - 1
	sum = 0
	for i < square_len && is_magic_square {
		sum += square[i][j]
		i++
		j--
	}
	if sum != magic_num {
		is_magic_square = false
	}
	// fmt.Println(sum)

	return is_magic_square
}

func main() {
	var x int = 0
	x += 1
	fmt.Println(x)
}