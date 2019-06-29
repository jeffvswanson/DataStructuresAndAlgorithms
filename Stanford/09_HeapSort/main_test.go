package main

import (
	"testing"
)

var a = []int{11, 13, 9, 4, 12, 9, 4, 8, 4}

func TestPrepend(t *testing.T) {
	h := heap{a}
	h.Prepend(0)
	expected := []int{0, 11, 13, 9, 4, 12, 9, 4, 8, 4}
	for idx, val := range expected {
		if val != h.xi[idx] {
			t.Errorf("At index %d, Expected: %d, Got: %d\n", idx, val, h.xi[idx])
		}
	}
}

func TestSwap(t *testing.T) {
	h := heap{[]int{0, 1, 2}}
	expected := []int{2, 1, 0}
	h.swap(0, 2)
	for idx, val := range expected {
		if val != h.xi[idx] {
			t.Errorf("At index %d, Expected: %d, Got: %d\n", idx, val, h.xi[idx])
		}
	}
}

func TestBubbleUp(t *testing.T) {
	var bubbleUpTests = []struct {
		i        int // index
		expected []int
	}{
		// Try to move the root
		{1, []int{0, 11, 13, 9, 4, 12, 9, 4, 8, 4}},
		// Try to move the last value
		{9, []int{0, 11, 13, 9, 4, 12, 9, 4, 8, 4}},
		// bubble up the number 12 in index position 5
		{5, []int{0, 11, 12, 9, 4, 13, 9, 4, 8, 4}},
	}

	h := heap{a}
	h.Prepend(0)
	for _, tt := range bubbleUpTests {
		h.bubbleUp(tt.i)
		for idx, val := range tt.expected {
			if val != h.xi[idx] {
				t.Errorf("At index %d, Expected: %d, Got: %d while trying to bubble up index %d\n",
					idx, val, h.xi[idx], tt.i)
			}
		}
	}
}

func TestHeapify(t *testing.T) {
	h := heap{a}
	h.Heapify()
	expected := []int{0, 4, 4, 4, 8, 12, 11, 9, 13, 9}
	for idx, val := range expected {
		if val != h.xi[idx] {
			t.Errorf("At index %d, Expected: %d, Got: %d\n", idx, val, h.xi[idx])
		}
	}
}

func TestLen(t *testing.T) {
	h := heap{a}
	h.Heapify()
	expected := len(h.xi) - 1
	got := h.Len()
	if got != expected {
		t.Errorf("Expected: %d, Got: %d\n", expected, got)
	}
}

func TestInsert(t *testing.T) {
	h := heap{a}
	h.Heapify()
	h.Insert(7)
	expected := []int{0, 4, 4, 4, 8, 7, 11, 9, 13, 9, 12}
	for idx, val := range expected {
		if val != h.xi[idx] {
			t.Errorf("At index %d, Expected: %d, Got: %d\n", idx, val, h.xi[idx])
		}
	}
}

func TestParentIndex(t *testing.T) {
	type expected struct {
		idx       int
		hasParent bool
	}
	var parentIndexTests = []struct {
		i int // index
		expected
	}{
		{0, expected{0, false}},
		{1, expected{0, false}},
		{3, expected{1, true}},
		{4, expected{2, true}},
	}

	for _, tt := range parentIndexTests {
		p, ok := parentIndex(tt.i)
		if p != tt.expected.idx {
			t.Errorf("parentIndex incorrect at index %d, Expected: %d, Got: %d\n",
				tt.i, tt.expected.idx, p)
		}
		if ok != tt.hasParent {
			t.Errorf("parentIndex error at index %d, Expected: %v, Got: %v\n",
				tt.i, tt.hasParent, ok)
		}
	}
}

func TestLeftIndex(t *testing.T) {
	type expected struct {
		idx      int
		hasChild bool
	}
	var childIndexTests = []struct {
		i int //index
		expected
	}{
		{0, expected{0, false}},
		{1, expected{2, true}},
		{3, expected{6, true}},
		{8, expected{0, false}},
	}

	h := heap{a}
	h.Heapify()

	for _, tt := range childIndexTests {
		c, ok := h.leftIndex(tt.i)
		if c != tt.idx {
			t.Errorf("leftIndex incorrect at index %d, Expected: %d, Got: %d\n",
				tt.i, tt.idx, c)
		}
		if ok != tt.hasChild {
			t.Errorf("leftIndex incorrect at index %d, Expected: %t, Got: %t\n",
				tt.i, tt.hasChild, ok)
		}
	}
}

func TestRightIndex(t *testing.T) {
	type expected struct {
		idx      int
		hasChild bool
	}
	var childIndexTests = []struct {
		i int //index
		expected
	}{
		{0, expected{0, false}},
		{1, expected{3, true}},
		{3, expected{7, true}},
		{8, expected{0, false}},
	}

	h := heap{a}
	h.Heapify()

	for _, tt := range childIndexTests {
		c, ok := h.rightIndex(tt.i)
		if c != tt.idx {
			t.Errorf("rightIndex incorrect at index %d, Expected: %d, Got: %d\n",
				tt.i, tt.idx, c)
		}
		if ok != tt.hasChild {
			t.Errorf("rightIndex incorrect at index %d, Expected: %t, Got: %t\n",
				tt.i, tt.hasChild, ok)
		}
	}
}

func TestBubbleDown(t *testing.T) {
	h := heap{a}
	h.Prepend(0)
	// Before Heapify 13 is in index position 2 with a child of 4
	// and grandchild of 4.
	h.bubbleDown(2)
	expected := []int{0, 11, 4, 9, 4, 12, 9, 4, 8, 13}
	for idx, val := range expected {
		if val != h.xi[idx] {
			t.Errorf("At index %d, Expected: %d, Got: %d while trying to bubble down index %d.\n",
				idx, val, h.xi[idx], 2)
		}
	}
}

func TestExtractMin(t *testing.T) {
	h := heap{a}
	h.Heapify()
	expected := []int{4, 4, 4, 8, 9, 9, 11, 12, 13}
	heapLength := h.Len()
	sortedList := make([]int, heapLength)
	for i := 0; i < heapLength; i++ {
		min, hasNode := h.ExtractMin()
		if hasNode {
			sortedList[i] = min
		}
	}
	for idx, val := range expected {
		if val != sortedList[idx] {
			t.Errorf("ExtractMin error at index %d, Expected: %d, Got: %d\n",
				idx, val, sortedList[idx])
		}
	}
}
