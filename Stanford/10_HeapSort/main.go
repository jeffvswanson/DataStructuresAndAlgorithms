package main

/*
Example of heapsort implementation using min-heap.

Demonstrates insertion into a heap data structure and extraction of the
minimum value from the heap to make a sorted slice.
*/

import "fmt"

type heap struct {
	xi []int
}

func main() {
	fmt.Println("This program provides an example of a min-heap sort.")
	a := []int{11, 13, 9, 4, 12, 9, 4, 8, 4}

	// Create the heap
	h := heap{a}
	fmt.Println("The original list:", h.xi)
	h.Heapify()

	fmt.Println("The slice after heapifying:", h.xi)

	// Sort the heap
	heapLength := h.Len()
	for i := 0; i < heapLength; i++ {
		min, hasNode := h.ExtractMin()
		if hasNode {
			a[i] = min
		}
	}
	fmt.Println("The sorted slice is:", a)
}

// Len returns the length of a 1-based index slice.
func (h *heap) Len() int {
	return len(h.xi) - 1
}

// Heapify turns the receiver into a slice in heap form.
func (h *heap) Heapify() {
	// Prepend a 0 into the 0 index
	h.Prepend(0)

	for idx := 1; idx < len(h.xi); idx++ {
		h.bubbleUp(idx)
	}
}

// Prepend adds the value, v, to the beginning of a slice.
func (h *heap) Prepend(v int) {
	h.xi = append(h.xi, v)
	copy(h.xi[1:], h.xi)
	h.xi[0] = v
}

// Insert the given key, k, into the heap
func (h *heap) Insert(k int) {
	h.xi = append(h.xi, k)
	h.bubbleUp(h.Len())
}

// bubbleUp moves the key at index, k, into position in the heap.
func (h *heap) bubbleUp(k int) {
	p, ok := parentIndex(k)
	if !ok {
		return // k is the root node
	}
	if h.xi[p] > h.xi[k] {
		h.swap(k, p)
		h.bubbleUp(p)
	}
}

func (h *heap) swap(a, b int) {
	h.xi[a], h.xi[b] = h.xi[b], h.xi[a]
}

// Return the index of the parent of the node at index k.
func parentIndex(k int) (int, bool) {
	// k is the root node
	if k < 2 {
		return 0, false
	}
	return k / 2, true
}

// Return the index of the left child for the parent node at index k.
func (h *heap) leftIndex(k int) (int, bool) {
	c := 2 * k
	if c > h.Len() || k == 0 {
		return 0, false
	}
	return c, true
}

// Return the index of the right child for the parent node at index k.
func (h *heap) rightIndex(k int) (int, bool) {
	c := 2*k + 1
	if c > h.Len() || k == 0 {
		return 0, false
	}
	return c, true
}

// ExtractMin returns the minimum value of the heap, the root.
func (h *heap) ExtractMin() (int, bool) {
	// Check if the heap only has the 0-element
	if h.Len() == 0 {
		return 0, false
	}
	root := h.xi[1]
	// Swap the value in the last index position into the root position.
	h.xi[1] = h.xi[h.Len()]
	h.xi = h.xi[:h.Len()]
	h.bubbleDown(1)
	return root, true
}

func (h *heap) bubbleDown(idx int) {
	min := idx
	// Find the smallest value between idx and the two children.
	left, ok := h.leftIndex(idx)
	if ok {
		if h.xi[min] > h.xi[left] {
			min = left
		}
	}
	r, ok := h.rightIndex(idx)
	if ok {
		if h.xi[min] > h.xi[r] {
			min = r
		}
	}
	if min != idx {
		h.swap(idx, min)
		h.bubbleDown(min)
	}
}
