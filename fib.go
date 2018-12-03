package main

import (
	"fmt"
	"os"
	"strconv"
)

var fibNumbers = make([]int, 0)

func calculateFib(x int) int {
	var prev, rv int = 1, 1
	fibNumbers = append(fibNumbers, prev)
	fibNumbers = append(fibNumbers, rv)
	for i := 2; i < x; i++ {
		old := rv
		rv += prev
		prev = old
		fibNumbers = append(fibNumbers, rv)
	}
	return rv
}

func main() {
	fib := calculateFib(10)
	file, err := os.Create("fib_output.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	fmt.Println(fib)
	fmt.Println(fibNumbers)
	file.WriteString(strconv.Itoa(fib))
}
