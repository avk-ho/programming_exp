// https://www.programmingexpert.io/programming-with-go/assessment/1

package main

import "fmt"

type Book struct {
	id int
	title string
	author string
	quantity int
}

type Library struct {
	books []*Book
}

func (li Library) CheckoutBook(id int) (*Book, bool) {
	var is_present bool
	var is_in_stock bool
	var book_pointer *Book = nil
	for _, book := range li.books {
		if book.id == id {
			is_present = true
			if book.quantity > 0 {
				book_pointer = book
				is_in_stock = true
				book.quantity -= 1
			}
		}
	}
	return book_pointer, is_in_stock && is_present
}

func (li Library) ReturnBook(id int) bool {
	var is_present bool

	for _, book := range li.books {
		if book.id == id {
			is_present = true
			book.quantity += 1
		}
	}
	return is_present
}

func main() {
	fmt.Println("hello")
}