package main

import "fmt"

type Name interface {
	GetName() string
}

type Person struct {
	firstName string
	lastName string

}

func (p Person) GetName() string {
	return p.firstName + " " + p.lastName
}

type Employee struct {
	name string
}

func (e Employee) GetName() string {
	return e.name
}

func PrintName(obj Name) {
	fmt.Println(obj.GetName())
}

func main() {
	var name Name = Person{"Tim", "Duval"}
	fmt.Println(name)
	fmt.Println(name.GetName())
	// fmt.Println(name.firstName) // returns an error because Name does not have firstName

	names := []Name{Employee{"Joe"}, Person{"Fred", "Bob"}}
	for _, name := range names {
		PrintName(name)
	}
	
}

type Comparable interface {
	Equals(obj Comparable) bool
}

type Vector struct {
	a int
	b int
}

func (v Vector) Equals(obj Vector) bool {
	if (v.a == obj.a) && (v.b == obj.b) {
		return true
	} else {
		return false
	}
}

type Rectangle struct {
	width float64
	height float64
}

func (r Rectangle) Equals(obj Rectangle) bool {
	same_height := r.height == obj.height
	same_width := r.width == obj.width
	same_reverse_h := r.height == obj.width
	same_reverse_w := r.width == obj.height

	if (same_height && same_width) || (same_reverse_h && same_reverse_w) {
		return true
	} else {
		return false
	}
}

type Addable interface {
	getNumericValue() float64
}

func AddAll(items []Addable) float64 {
	// Write your code here.
	var sum float64 = 0

	for _, item := range items {
		val := item.getNumericValue()
		sum = sum + val
	}

	return sum
}
