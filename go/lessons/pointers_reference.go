package main

import "fmt"

func change(x *int) {
	*x = 2
}

type Book struct {
	title string
	id int
}

func changeTitle(book *Book, title string) {
	book.title = title
}

func (b *Book) changeId(id int) {
	b.id = id
}

func main() {
	x := 0
	y := &x
	*y = 10
	fmt.Println(x, y)

	z := 0
	change(&z)
	fmt.Println(z)

	a := []string{"hello", "world"}
	b := &x
	c := &b

	fmt.Println(a, b, c)
	fmt.Println(a, *b, *c)
	fmt.Println(a, *b, **c)

	book := Book{"Harry P", 1}
	changeTitle(&book, "new HP")
	fmt.Println(book)

}

func Swap(p1 *int, p2 *int) {
    temp := *p1
    *p1 = *p2
    *p2 = temp
}

type Team struct {
	name string
	wins int
	ties int
}

func GetBestTeam(pointers []*Team) *Team {
	var bestTeam *Team = nil
	max_score := -1

	for _, team := range pointers {
		score := team.wins * 3 + team.ties
		if score > max_score {
			max_score = score
			bestTeam = team
		}
	}

	return bestTeam
}