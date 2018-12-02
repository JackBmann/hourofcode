package main

import "fmt"

func fib(x int) int {
	var prev, rv int = 1, 1
	for i := 2; i < x; i++ {
		old := rv
		rv += prev
		prev = old
	}
	return rv
}

func main() {
	fmt.Println(fib(10))
}
