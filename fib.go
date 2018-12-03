package main

import (
	"fmt"
	"os"
	"strconv"
)

func calculateFib(x int) int {
	var prev, rv int = 1, 1
	for i := 2; i < x; i++ {
		old := rv
		rv += prev
		prev = old
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
	file.WriteString(strconv.Itoa(fib))
}
