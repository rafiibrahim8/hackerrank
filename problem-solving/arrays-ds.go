// https://www.hackerrank.com/challenges/arrays-ds/problem

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}
	s := ""
	for i := n - 1; i >= 0; i-- {
		s = s + " " + strconv.Itoa(arr[i])
	}
	fmt.Println(strings.TrimSpace(s))
}
