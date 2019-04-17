package main

/*
Programming question 2 from Stanford Datastructures and Algorithms

The file, quicksort.txt, contains all of the integers between 1 and
10,000 inclusive, with no repeats) in unsorted order. The integer in
the i-th row of the file gives you the i-th entry of an input array.

Your task is to compute the total number of comparisons used to sort
the given input file by QuickSort. As you know, the number of
comparisons depends on which elements are chosen as pivots, so we'll
ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a
recursive call on a subarray of length m, you should simply add m-1 to
your running total of comparisons. (This is because the pivot element
is compared to each of the other m - 1 elements in the subarray in this
recursive call.)

WARNING: The Partition subroutine can be implemented in several
different ways, and different implementations can give you differing
numbers of comparisons. For this problem, you should implement the
Partition subroutine exactly as it is described in the video lectures
(otherwise you might get the wrong answer).

Question 1
For the first part of the programming assignment, you should always use
the first element of the array as the pivot element.

Question 2
Compute the number of comparisons (as in Problem 1), always using the
final element of the given array as the pivot element. Again, be sure
to implement the Partition subroutine exactly as it is described in
the video lectures.

Question 3
Compute the number of comparisons (as in Problem 1), using the
"median-of-three" pivot rule. [The primary motivation behind this rule
is to do a little bit of extra work to get much better performance on
input arrays that are nearly sorted or reverse sorted.] In more
detail, you should choose the pivot as follows. Consider the first,
middle, and final elements of the given array. (If the array has odd
length it should be clear what the "middle" element is; for an array
with even length 2k, use the k-th element as the "middle" element. So
for the array 4 5 6 7, the "middle" element is the second one ---- 5
and not 6!) Identify which of these three elements is the median
(i.e., the one whose value is in between the other two), and use this
as your pivot. As discussed in the first and second parts of this
programming assignment, be sure to implement Partition exactly as
described in the video lectures (including exchanging the pivot
element with the first element just before the main Partition
subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first
(8), middle (4), and last (1) elements; since 4 is the median of the
set {1,4,8}, you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons
made in identifying the median of the three candidate elements. You
should NOT do this. That is, as in the previous two problems, you
should simply add m - 1 to your running total of comparisons every
time you recurse on a subarray with length m.
*/

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	fmt.Println("Setting up.")
	initialSlice := setup()

	// Set up slices to aggregate number of comparisons used per pivot
	// selection method.
	comparisons := make([]int, 3)
	pivotMethods := []string{"first", "last", "median"}

	for i, pivotMethod := range pivotMethods {
		fmt.Printf("Using %v pivot method to calculate comparisons.\n", pivotMethod)

		// Copy the initial slice to prevent Go from referencing the memory
		// location of the slice
		quicksortSlice := make([]int, len(initialSlice))
		copy(quicksortSlice, initialSlice)

		_, comparisons[i] = quicksort(quicksortSlice, 0, len(quicksortSlice)-1, pivotMethod)
	}

	fmt.Println("Calculations complete.")

	for i, pivotMethod := range pivotMethods {
		fmt.Printf("There are %d comparisons using the %v element as the pivot element.\n", comparisons[i], pivotMethod)
	}
}

func setup() []int {
	file, err := os.Open("QuickSort.txt")
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return []int{0, 1}
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	var xint []int
	for _, value := range lines {
		newValue, _ := strconv.Atoi(value)
		xint = append(xint, newValue)
	}

	return xint
}

func quicksort(xint []int, leftIndex, rightIndex int, pivotMethod string) ([]int, int) {
	// Quicksort algorithm

	// boundedListLength = m - 1
	boundedListLength := rightIndex - leftIndex
	// Base case: A difference less than 1 between the left and right
	// indices means the element is sorted and no comparisons are made.
	if boundedListLength < 1 {
		return xint, 0
	}

	pivotIndex := selectPivot(xint, leftIndex, rightIndex, pivotMethod)
	pivotValue := xint[pivotIndex]

	// Swap the pivot with the element in the leftmost index position.
	if pivotIndex != leftIndex {
		xint = swap(xint, leftIndex, pivotIndex)
	}

	// Set pointers for partitions
	// i is the pointer for the index where all elements in positions
	// less than index i are less than the pivot
	// j is the pointer to the index where all elements in positions
	// greater than index j have not yet been compared to the pivot.
	i := leftIndex + 1 // The pivot element is in the first position.
	j := i

	for j <= rightIndex {
		if xint[j] <= pivotValue {
			xint = swap(xint, i, j)
			i++
		}
		j++
	}

	// Swap the pivot element into its rightful position.
	xint = swap(xint, leftIndex, i-1)

	comparisons := boundedListLength
	var lowComparisons, highComparisons int

	// Sort the elements less than the pivot
	xint, lowComparisons = quicksort(xint, leftIndex, i-2, pivotMethod)
	// Sort the element greater than the pivot
	xint, highComparisons = quicksort(xint, i, j-1, pivotMethod)

	// Accumulate the number of comparisons
	comparisons += lowComparisons + highComparisons

	return xint, comparisons
}

func selectPivot(xint []int, leftIndex, rightIndex int, pivotMethod string) int {
	// Selects which quicksort pivot method to use.

	var pivotIndex int

	switch pivotMethod {
	case "first":
		pivotIndex = leftIndex
	case "last":
		pivotIndex = rightIndex
	case "median":
		// pivotIndex = "median of three"
		firstElement := xint[leftIndex]
		lastElement := xint[rightIndex]

		// Determine the median value of the bounded slice.
		boundedSliceLength := rightIndex - leftIndex
		medianIndex := boundedSliceLength/2 + leftIndex
		medianElement := xint[medianIndex]

		potentialMedianList := []int{firstElement, medianElement, lastElement}
		potentialMedianList = selectionSort(potentialMedianList)

		medianOfThree := potentialMedianList[1]

		if firstElement == medianOfThree {
			pivotIndex = leftIndex
		} else if medianElement == medianOfThree {
			pivotIndex = medianIndex
		} else {
			pivotIndex = rightIndex
		}
	default:
		// pivotIndex = randomly chosen index position
		r := rand.New(rand.NewSource(time.Now().UnixNano()))
		pivotIndex = rightIndex - r.Intn(rightIndex-leftIndex+1)
	}

	return pivotIndex
}

func swap(xint []int, i, j int) []int {
	// Swaps elements i and j in slice, xint.

	tmp := xint[i]
	xint[i] = xint[j]
	xint[j] = tmp

	return xint
}

func selectionSort(xint []int) []int {
	for idx, value := range xint {
		minValue := value
		minIndex := idx
		j := idx + 1
		for j < len(xint) {
			if xint[j] < minValue {
				minValue = xint[j]
				minIndex = j
			}
			j++
		}
		xint = swap(xint, idx, minIndex)
	}

	return xint
}
