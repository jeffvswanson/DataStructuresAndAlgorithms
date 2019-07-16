/*
With the following text file: Median.txt

The goal of this problem is to implement the "Median Maintenance"
algorithm (covered in the Week 5 lecture on heap applications). The
text file contains a list of the integers from 1 to 10000 in
unsorted order; you should treat this as a stream of numbers, arriving
one by one. Letting x-subscript i denote the i-th number of the file,
the k-th median m-subscript k is defined as the median of the numbers
x-subscript 1,..., x-subscript k. (So, if k is odd, then m-subscript k
is ((k+1)/2)th smallest number among x-subscript 1,...,x-subscript k;
if k is even, then m-subscript k is the (k/2)th smallest number among
x-subscript 1,...,x-subscript k.)

Find the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). That is, you should compute
(m-subscript 1 + m-subscript 2 + ... + m-subscript 10000) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.
*/
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

type heap struct {
	Type string
	xi   []int
}

func main() {

	f, err := os.Open("Median.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	// highValHeap stores the higher half of elements in the set in a min-heap.
	highValHeap := heap{Type: "min"}

	// lowValHeap storse the lower half of elements in the set in a max-heap.
	lowValHeap := heap{Type: "max"}

	median, medianTotal := 0, 0

	s := bufio.NewScanner(f)
	s.Split(bufio.ScanLines)

	for s.Scan() {
		x, err := strconv.Atoi(s.Text())
		if err != nil {
			fmt.Println(err)
		}

		// Put x into the correct heap.
		// If x > median, place x in highValHeap.
		if x > median {
			highValHeap.insert(x)
		} else {
			lowValHeap.insert(x)
		}

		// Check if heaps need to be rebalanced
		rebalance(&lowValHeap, &highValHeap)

		// Calculate the median given the new x
		median = findMedian(&lowValHeap, &highValHeap)

		// Add the median to the medianTotal.
		medianTotal += median
	}

	// Once the file is exhausted returnValue = medianTotal%10000.
	output := findLastFour(medianTotal)
	fmt.Printf("The last four digits of the sums of the medians is %d\n", output)
}

// findLastFour returns the last four numbers of an integer.
func findLastFour(x int) int {
	return x % 10000
}

// findMedian determines the median value between the two heaps.
func findMedian(lowValHeap, highValHeap *heap) int {

	count := lowValHeap.hLen() + highValHeap.hLen()
	// i is the median's index
	i, median := 0, 0

	if count%2 == 0 {
		i = count / 2
	} else {
		i = (count + 1) / 2
	}

	if i > lowValHeap.hLen() {
		median, _ = highValHeap.peek()
	} else {
		median, _ = lowValHeap.peek()
	}

	return median
}

// rebalance ensures the two input heaps remain within one element
// of one another.
func rebalance(h1, h2 *heap) {

	if math.Abs(float64(h1.hLen())-float64(h2.hLen())) > 1 {
		if h1.hLen() > h2.hLen() {
			root, prs := h1.extractRoot()
			if prs {
				h2.insert(root)
			}
		} else {
			root, prs := h2.extractRoot()
			if prs {
				h1.insert(root)
			}
		}
		rebalance(h1, h2)
	}
}

// hLen returns the length of a slice with a 1-based index.
func (h *heap) hLen() int {
	return len(h.xi) - 1
}

// insert the given key, k, into the heap.
func (h *heap) insert(k int) {

	// The max heap type has the insertion value negated to allow a
	// min heap structure that will organize by max values.
	// The inserted value gets converted back to its correct value
	// on a peek or extraction.
	if h.Type == "max" {
		h.xi = append(h.xi, -k)
	} else {
		h.xi = append(h.xi, k)
	}
	h.bubbleUp(h.hLen())
}

// extractRoot returns the minimum value of the heap, the root.
func (h *heap) extractRoot() (int, bool) {
	// Check if the heap only has the 0-element
	if h.hLen() == 0 {
		return 0, false
	}

	var root int
	if h.Type == "max" {
		root = -h.xi[1]
	} else {
		root = h.xi[1]
	}
	// Swap the last index position into the root node.
	h.xi[1] = h.xi[h.hLen()]
	// Pare down the list since the last node becam the root
	h.xi = h.xi[:h.hLen()-1]

	if h.hLen() > 1 {
		h.bubbleDown(1)
	}
	return root, true
}

// bubbleUp moves the key at index, i, into position in the heap.
func (h *heap) bubbleUp(i int) {
	p, ok := parentIndex(i)
	if !ok {
		return // k is the root node
	}
	if h.xi[p] > h.xi[i] {
		h.swap(i, p)
		h.bubbleUp(p)
	}
}

// bubbleDown moves a misplaced node into its appropriate position to
// maintain the heap property using its index.
func (h *heap) bubbleDown(i int) {

	// Find the smaller of the two values between the node at i and i's
	// two children.
	min := i
	left, prs := h.leftIndex(i)
	if prs {
		if h.xi[i] > h.xi[left] {
			min = left
		}
	}
	r, prs := h.rightIndex(i)
	if prs {
		if h.xi[i] > h.xi[r] {
			min = r
		}
	}
	if min != i {
		h.swap(i, min)
		h.bubbleDown(min)
	}

}

// peek returns the value at the root of a heap, but does not remove it.
func (h *heap) peek() (int, bool) {

	root := 0
	// Check if the heap only has the 0-element.
	// False return because there is no root element.
	if h.hLen() < 1 {
		return root, false
	}

	if h.Type == "max" {
		root = -h.xi[1]
	} else {
		root = h.xi[1]
	}

	return root, true
}

// swap swaps the position of two values with one another.
func (h *heap) swap(a, b int) {
	h.xi[a], h.xi[b] = h.xi[b], h.xi[a]
}

// parentIndex returns the index of the parent node to the node a index i.
func parentIndex(i int) (int, bool) {
	// i is the root node and therefore has no parent.
	if i < 2 {
		return 0, false
	}
	return i / 2, true
}

// leftIndex returns the left child index for the parent node at index i.
func (h *heap) leftIndex(i int) (int, bool) {
	c := 2 * i
	if c > h.hLen() || i == 0 {
		return 0, false
	}
	return c, true
}

// rightIndex returns the right child index for the parent node at index i.
func (h *heap) rightIndex(i int) (int, bool) {
	c := 2*i + 1
	if c > h.hLen() || i == 0 {
		return 0, false
	}
	return c, true
}
