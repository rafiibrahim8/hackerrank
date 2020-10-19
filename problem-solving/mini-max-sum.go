// https://www.hackerrank.com/challenges/mini-max-sum/problem

package main

import (
	"fmt"
	"sort"
)

func sum(arr []int) int64 {
	res := int64(0)
	for _, value := range arr {
		res += int64(value)
	}
	return res
}

func main() {
	var n [5]int
	for i := 0; i < 5; i++ {
		fmt.Scan(&n[i])
	}
	sort.Ints(n[:])
	fmt.Println(sum(n[0:4]), sum(n[1:5]))
}
