package main

// An example of the merge sort algorithm

import "fmt"

func main() {
	A := []int{5, 4, 1, 8, 7, 2, 6, 3, 9}
	fmt.Printf("The original slice is %v.", A)
	A = divideAndConquer(A)
	fmt.Printf("\nThe sorted slice is %v.", A)
}

func divideAndConquer(xi []int) []int {
	// Base case: A single element or an empty slice is sorted.
	if len(xi) < 2 {
		return xi
	}

	// Split the original slice in half to get to the base case with recursion
	a := divideAndConquer(xi[0 : len(xi)/2])
	b := divideAndConquer(xi[len(xi)/2:])

	sortedSlice := mergeSort(a, b)

	return sortedSlice
}

func mergeSort(a, b []int) []int {
	mergedSlice := make([]int, len(a)+len(b))

	// Initialize indices for arrays a and b
	var i, j int

	for k := 0; k < len(mergedSlice); k++ {
		// Check if we've exhausted a slice and copy remaining elements from the second slice
		if i >= len(a) {
			for j < len(b) {
				mergedSlice[k] = b[j]
				j++
				// Increment k because we won't break out of this internal loop
				k++
			}
			break
		} else if j >= len(b) {
			for i < len(a) {
				mergedSlice[k] = a[i]
				i++
				// Increment k because we won't break out of this internal loop
				k++
			}
			break
		}

		// Merging the slices
		if a[i] <= b[j] {
			mergedSlice[k] = a[i]
			i++
		} else {
			mergedSlice[k] = b[j]
			j++
		}
	}

	return mergedSlice
}
