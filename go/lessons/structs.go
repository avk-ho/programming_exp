package main

import "fmt"

type Person struct {
	name string
	age uint
	clothing Clothing
}

type Clothing struct {
	shoeSize uint
	shirtColor string
}

func (c Clothing) GetShoeSize() uint {
	return c.shoeSize
}

func (p Person) GetName() string {
	return p.name
}

// func (p Person) SetName(newName string) {
// 	p.name = newName
// 	fmt.Println(p)
// }

func main() {
	p1 := Person{"Tim", 21, Clothing{12, "Blue"}}
	fmt.Println(p1)
	shoeSize := p1.clothing.GetShoeSize()
	fmt.Println(shoeSize)
}


type ContactInformation struct {
	address string
	city    string
	state   string
	country string
}

type Employee struct {
	firstName string
	lastName  string
	salary    float64
	contact   ContactInformation
}

func (e Employee) GetName() string {
	return e.firstName + " " + e.lastName
}

func (e Employee) TaxRate(otherIncome float64) int {
	totalIncome := e.salary + otherIncome
	if totalIncome < 25000 {
		return 20
	} else if totalIncome < 50000 {
		return 25
	} else if totalIncome < 75000 {
		return 30
	} else if totalIncome < 100000 {
		return 35
	} else {
		return 40
	}
}