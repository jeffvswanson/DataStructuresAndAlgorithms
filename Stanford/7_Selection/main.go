package main

// An example of a linear runtime selection algorithm leveraging quicksort
// principles.

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	targetSlice := []int{7, 0, 1, 2, 5, 8, 6, 3, 9, 4}
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	kOrderStat := 1 + r.Intn(len(targetSlice))

	fmt.Println("The list in question is:\t", targetSlice)

	_, targetValue := quickSelect(targetSlice, kOrderStat)

	lastDigit := kOrderStat % 10

	if lastDigit == 1 {
		fmt.Printf("The %dst order statistic is %d.\n", kOrderStat, targetValue)
	} else if lastDigit == 2 {
		fmt.Printf("The %dnd order statistic is %d.\n", kOrderStat, targetValue)
	} else if lastDigit == 3 {
		fmt.Printf("The %drd order statistic is %d.\n", kOrderStat, targetValue)
	} else {
		fmt.Printf("The %dth order statistic is %d.\n", kOrderStat, targetValue)
	}
}

func quickSelect(targetSlice []int, k int) ([]int, int) {
	// Base case: A slice of length 1 or 0 is sorted by default.
	if len(targetSlice) < 2 {
		return targetSlice, targetSlice[0]
	}

	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	pivotIndex := r.Intn(len(targetSlice) - 1)
	pivotValue := targetSlice[pivotIndex]

	// Swap the pivot index with the leftmost element.
	targetSlice = swap(targetSlice, pivotIndex, 0)

	// Set pointers for partitions.
	// i is the pointer for the index where all elements in positions
	// less than index i are less than or equal to the pivot.
	// j is the pointer to the index where all elements in positions
	// greater than the index j have not yet been compared to the pivot.
	i := 1
	j := 1

	for j < len(targetSlice) {
		if targetSlice[j] < pivotValue {
			targetSlice = swap(targetSlice, i, j)
			i++
		}
		j++
	}

	// Set the index of where the pivot should reside.
	pivotIndex = i - 1

	// Place the pivot in its rightful place.
	targetSlice = swap(targetSlice, 0, pivotIndex)

	// Determine how to continue solving the problem.
	// Remember, k is on a 1-based index and pivotIndex is 0-based.
	if k-1 == pivotIndex {
		return targetSlice, targetSlice[pivotIndex]
	} else if k-1 < pivotIndex {
		return quickSelect(targetSlice[:pivotIndex], k)
	} else {
		return quickSelect(targetSlice[i:], k-i)
	}
}

func swap(xint []int, i, j int) []int {
	xint[i], xint[j] = xint[j], xint[i]

	return xint
}
