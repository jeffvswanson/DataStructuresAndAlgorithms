package main

// A program to show how to implement quicksort in an average of O(n lg n)
// runtime.

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	targetSlice := []int{0, 7, 1, 2, 5, 8, 6, 3, 9, 4}

	fmt.Println("The initial unsorted slice is:\t", targetSlice)

	targetSlice = quicksort(targetSlice, 0, len(targetSlice)-1)

	fmt.Println("The quicksorted slice is:\t", targetSlice)
}

func quicksort(xint []int, leftIndex, rightIndex int) []int {
	// Base case: A difference of 1 or 0 between the left and right index means
	// the element is sorted.
	if rightIndex-leftIndex < 1 {
		return xint
	}

	r := rand.New(rand.NewSource(time.Now().UnixNano()))

	pivotIndex := rightIndex - r.Intn(rightIndex-leftIndex+1)
	pivot := xint[pivotIndex]

	// Swap the pivot element with the element in the leftmost index position
	xint = swap(xint, leftIndex, pivotIndex)

	/* Set pointers for partitions
	   i is the pointer for the index where all elements in positions less than
	   index i are less than the pivot.
	   j is the pointer to the index where all elements in positions greater
	   than index j have not yet been compared to the pivot.
	*/

	i := leftIndex + 1 // The pivot element is in the first position
	j := i

	for j <= rightIndex {
		if xint[j] < pivot {
			xint = swap(xint, i, j)
			i++
		}
		j++
	}

	// Swap the pivot element into its rightful position
	xint = swap(xint, i-1, leftIndex)

	// Sort the elements less than the pivot
	xint = quicksort(xint, leftIndex, i-2)
	// Sort the elements greater than the pivot
	xint = quicksort(xint, i, len(xint)-1)

	return xint
}

func swap(xint []int, i, j int) []int {
	// Swap the elements at i and j in the slice, xint.
	tmp := xint[i]
	xint[i] = xint[j]
	xint[j] = tmp

	return xint
}
