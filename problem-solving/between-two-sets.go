// https://www.hackerrank.com/challenges/between-two-sets/problem

package main

import "fmt"

func getTotalX(a []uint8, b []uint8) uint8 {
	var t, tx, ty uint8
	min := findMin(b)
	for i := uint8(1); i <= min; i++ {
		tx = 0
		for _, j := range a {
			if i%j == 0 {
				tx++
			} else {
				break
			}
		}
		if tx == uint8(len(a)) {
			ty = 0
			for _, j := range b {
				if j%i == 0 {
					ty++
				} else {
					break
				}
			}
			if ty == uint8(len(b)) {
				t++
			}
		}
	}
	return t
}

func findMin(arr []uint8) uint8 {
	min := uint8(255)
	for _, value := range arr {
		if value < min {
			min = value
		}
	}
	return min
}

func scanArr(length uint8) []uint8 {
	arr := make([]uint8, length)
	for i := uint8(0); i < length; i++ {
		fmt.Scan(&arr[i])
	}
	return arr
}

func main() {
	var n, m uint8
	fmt.Scan(&n, &m)
	a := scanArr(n)
	b := scanArr(m)
	fmt.Println(getTotalX(a, b))
}
