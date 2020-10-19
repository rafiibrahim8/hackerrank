// https://www.hackerrank.com/challenges/plus-minus/problem
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var n, p, m, z uint8
	fmt.Scanln(&n)
	scanner.Scan()
	str := scanner.Text()
	for _, e := range strings.Split(str, " ") {
		//fmt.Println(i, e)
		x, _ := strconv.Atoi(e)
		if x > 0 {
			p++
		} else if x < 0 {
			m++
		} else {
			z++
		}
	}
	fmt.Printf("%.6f\n", float32(p)/float32(n))
	fmt.Printf("%.6f\n", float32(m)/float32(n))
	fmt.Printf("%.6f\n", float32(z)/float32(n))
}
