package main

// An example of using the deterministic "median of medians" method to
// conduct a selection in linear, O(n), runtime.

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

func main() {
	targetSlice := []int{7, 2, 17, 12, 13, 8, 20, 4, 6, 3, 19, 1, 9, 5, 16,
		10, 15, 18, 14, 11}

	kOrderStat := genKOrderStat(len(targetSlice))

	_, targetValue := quickSelect(targetSlice, kOrderStat)

	lastDigit := findLastDigit(kOrderStat)

	fmt.Println("From the list")
	sort.Ints(targetSlice)
	fmt.Println(targetSlice)
	result := genOutput(kOrderStat, targetValue, lastDigit)
	fmt.Println(result)
}

func genKOrderStat(sliceLength int) int {

	// Possible strategy to implement a uniform distribution of integers
	// Use Source (source of uniformly-distributed pseudo-random int64 values in the range [0, 1<<63))
	// Use a modulo operator to shoehorn the values into the range I want.
	// For example, 1<<63 = 9223372036854775807
	// If I want values distributed between 1 and 20 inclusive
	// kOrderStat := 1 + uniformRandomValue%(upperLimit+1)

	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	kOrderStat := r.Intn(sliceLength) + 1

	return kOrderStat
}

func quickSelect(xint []int, k int) ([]int, int) {
	// Base case: A list of length 1 or 0 is sorted by default.
	if len(xint) < 2 {
		return xint, xint[0]
	}

	pivotIndex := findMedianOfMedians(xint)
	pivotValue := xint[pivotIndex]

	// Swap the pivot value to the leftmost index position
	xint = swap(xint, 0, pivotIndex)

	// Set up the pointers
	// i is the index delineating the partition between all values less
	// than or equal to the pivot.
	// j is the index value of which all indices greater than j have
	// not yet been compared against the pivot value.
	i := 1
	j := 1

	// Perform the sort
	for j < len(xint) {
		if xint[j] <= pivotValue {
			xint = swap(xint, i, j)
			i++
		}
		j++
	}

	// Swap the pivot value into its rightful position.
	pivotIndex = i - 1
	xint = swap(xint, 0, pivotIndex)

	// Determine how to continue solving the problem.
	// Remember, k is on a 1-based index and pivotIndex is 0-based
	if k-1 == pivotIndex {
		return xint, xint[pivotIndex]
	} else if k-1 < pivotIndex {
		return quickSelect(xint[:pivotIndex], k)
	} else {
		return quickSelect(xint[i:], k-i)
	}
}

func findMedianOfMedians(xint []int) int {
	// Function to select the median of medians from the given slice.

	groupSize := 5
	xintLen := len(xint)

	// Base case: A list less than the group size is close enough.
	if xintLen < groupSize {
		return xintLen / 2
	}

	numFullGroups := xintLen / groupSize
	medians := make([]int, numFullGroups)
	medianIndices := make([]int, numFullGroups)
	var medianOfMediansIndex int

	for i := 0; i < numFullGroups; i++ {
		startIndex := i * 5
		xint = selectionSort(xint, startIndex, startIndex+5)
		medians[i] = xint[startIndex+2]
		medianIndices[i] = startIndex + 2
	}

	_, medianOfMedians := quickSelect(medians, xintLen/(groupSize*2))

	for idx, potentialMedian := range medians {
		if potentialMedian == medianOfMedians {
			medianOfMediansIndex = medianIndices[idx]
		}
	}

	return medianOfMediansIndex
}

func selectionSort(xint []int, leftIndex, rightIndex int) []int {
	// Will always sort 5 elements. Used to determine median values.

	for i := leftIndex; i < rightIndex; i++ {
		minValue := xint[i]
		minIndex := i
		j := i + 1
		for j < rightIndex {
			if xint[j] < minValue {
				minValue = xint[j]
				minIndex = j
			}
			j++
		}
		xint = swap(xint, i, minIndex)
	}

	return xint
}

func swap(xint []int, i, j int) []int {
	// Swaps values at indices i and j in slice xint.

	xint[i], xint[j] = xint[j], xint[i]
	return xint
}

func findLastDigit(n int) int {
	// Determines the last digit in a base 10 integer.

	return n % 10
}

func genOutput(kOrderStat, targetValue, lastDigit int) string {
	var result string

	if kOrderStat != 11 && lastDigit == 1 {
		result = fmt.Sprintf("The %dst order statistic is %d.", kOrderStat,
			targetValue)
	} else if kOrderStat != 12 && lastDigit == 2 {
		result = fmt.Sprintf("The %dnd order statistic is %d.", kOrderStat,
			targetValue)
	} else if kOrderStat != 13 && lastDigit == 3 {
		result = fmt.Sprintf("The %drd order statistic is %d.", kOrderStat,
			targetValue)
	} else {
		result = fmt.Sprintf("The %dth order statistic is %d.", kOrderStat,
			targetValue)
	}
	return result
}
