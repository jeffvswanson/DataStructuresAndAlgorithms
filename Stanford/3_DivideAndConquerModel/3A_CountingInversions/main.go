package main

// An example program to demonstrate counting inversions between two slices
// in O(n lg n) time using principles of merge sort.

import "fmt"

func main() {
	xi := []int{1, 5, 3, 6, 4, 2}
	fmt.Println("The input slice is", xi)
	fmt.Println("The comparision slice is [1 2 3 4 5 6]")

	numInversions := sortAndCountInversions(xi)

	fmt.Printf("\nThere are %d inversions between the two lists.", numInversions)
}

func sortAndCountInversions(xi []int) int {
	// Base case: An empty slice or slice of length 1 is by default sorted and
	// contains no inversions.
	if len(xi) < 2 {
		return 0
	}

	// Divide with recursion
	sliceLowerHalf := xi[0 : len(xi)/2]
	sliceUpperHalf := xi[len(xi)/2:]

	numLeftInversions := sortAndCountInversions(sliceLowerHalf)
	numRightInversions := sortAndCountInversions(sliceUpperHalf)

	// Conquer with merge sort principles
	numSplitInversions := countSplitInversions(sliceLowerHalf, sliceUpperHalf)

	return numLeftInversions + numRightInversions + numSplitInversions
}

func countSplitInversions(xLower, xUpper []int) int {
	// Initialize counter and indices
	var countInversions, i, j int

	for k := 0; k < len(xLower)+len(xUpper); k++ {
		// Check if we've exhausted all values in one of the slices
		if i >= len(xLower) {
			// All values left in xUpper were greater than any value in xLower
			break
		} else if j >= len(xUpper) {
			// All values left in xLower are greater than any value in xUpper
			// and are inversions
			for i < len(xLower) {
				countInversions += len(xLower) - i
				i++
			}
			break
		}

		// Not an inversion
		if xLower[i] < xUpper[j] {
			i++
		} else {
			countInversions += len(xLower) - i
			j++
		}
	}
	return countInversions
}
