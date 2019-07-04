/*
Using algo1-programming_prob-2sum.txt.

The goal of this problem is to implement a variant of the 2-SUM
algorithm (covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative
(there might be some repetitions!).This is your array of integers,
with the i-th row of the file specifying the i-th entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x, y in
the input file that satisfy x+y=t. (NOTE: ensuring distinctness
requires a one-line addition to the algorithm from the lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space
provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try
implementing your own hash table for it. For example, you could compare
performance under the chaining and open addressing approaches to
resolving collisions.
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// Insert elements in the .txt into a hash table, h, ensuring
	// duplicate elements are not inserted.
	// Create second list, targets, for the values -10000 to 10000
	// inclusive.
	h, targets := setup()

	// For each value, x, in the .txt file, check if there is a
	// value, y, in h that satisfies t-x=y.
	// After going through all the values return the count of targets
	// found.
	found := twoSumSearch(h, targets)

	fmt.Printf("The number of target values found to have sums was %d.\n", found)
}

func setup() (map[int64]bool, map[int64]bool) {

	values := make(map[int64]bool)
	targets := make(map[int64]bool)

	var lb, ub int64
	lb = -10000
	ub = 10000
	for i := lb; i <= ub; i++ {
		targets[i] = true
	}

	f, err := os.Open("algo1-programming_prob-2sum.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		v, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			fmt.Println(err)
		}
		values[v] = true
	}
	return values, targets
}

func twoSumSearch(h, targets map[int64]bool) int {

	finalMap := make(map[int64]bool)

	for k, v := range targets {
		finalMap[k] = v
	}

	for t := range targets {
		for x := range h {
			if _, ok := h[t-x]; ok {
				delete(finalMap, t)
				break
			}
		}
	}
	return len(targets) - len(finalMap)
}
