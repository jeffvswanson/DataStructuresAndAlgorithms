package main

import "testing"

func TestFindLastFour(t *testing.T) {
	tests := map[string]struct {
		input int
		want  int
	}{
		"less than 10,000":    {input: 100, want: 100},
		"equals 10000":        {input: 10000, want: 0},
		"greater than 10,000": {input: 15156, want: 5156},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			got := findLastFour(cond.input)
			if got != cond.want {
				t.Fatalf("expected: %d, got: %v\n", cond.want, got)
			}
		})
	}
}

func TestParentIndex(t *testing.T) {
	type want struct {
		parentIndex int
		hasParent   bool
	}

	tests := map[string]struct {
		input int
		want
	}{
		"empty heap":         {input: 0, want: want{0, false}},
		"root has no parent": {input: 1, want: want{0, false}},
		"node has parent":    {input: 6, want: want{3, true}},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			got, ok := parentIndex(cond.input)
			if got != cond.want.parentIndex || ok != cond.want.hasParent {
				t.Fatalf("expected: %d, %t; got: %d, %t\n", cond.want.parentIndex, cond.want.hasParent, got, ok)
			}
		})
	}
}

func TestHLen(t *testing.T) {

	// Remember, all heaps are initialized with a 0 in the 0-index position
	// as heaps are based on a 1-based index.
	emptyHeap := heap{Type: "min", xi: []int{0}}
	minHeap := heap{Type: "min", xi: []int{0, 1}}
	// The max heap is constructed from negating input values
	maxHeap := heap{Type: "max", xi: []int{0, -10, -9, -8, -7, -6}}

	tests := map[string]struct {
		input heap
		want  int
	}{
		"empty heap":            {input: emptyHeap, want: 0},
		"1-element heap":        {input: minHeap, want: 1},
		"multiple element heap": {input: maxHeap, want: 5},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			got := cond.input.hLen()
			if got != cond.want {
				t.Fatalf("expected: %d, got: %d\n", cond.want, got)
			}
		})
	}
}

func TestSwap(t *testing.T) {

	testHeap := heap{Type: "min", xi: []int{0, 1, 2}}
	want := []int{0, 2, 1}

	testHeap.swap(1, 2)
	for i, v := range testHeap.xi {
		if v != want[i] {
			t.Fatalf("at index position %d on swap() - expected: %d, got %d\n", i, want[i], v)
		}
	}
}

func TestPeek(t *testing.T) {

	// Remember, all heaps are initialized with a 0 in the 0-index position
	// as heaps are based on a 1-based index.
	emptyHeap := heap{Type: "min", xi: []int{0}}
	minHeap := heap{Type: "min", xi: []int{0, 1, 2, 3, 4, 5}}
	// The max heap is constructed from negating input values.
	maxHeap := heap{Type: "max", xi: []int{0, -10, -9, -8, -7, -6}}

	type want struct {
		root    int
		hasRoot bool
	}

	tests := map[string]struct {
		input heap
		want
	}{
		"empty heap": {emptyHeap, want{0, false}},
		"min heap":   {minHeap, want{1, true}},
		"max heap":   {maxHeap, want{10, true}},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			got, prs := cond.input.peek()
			if got != cond.want.root || prs != cond.want.hasRoot {
				t.Fatalf("expected: %d, %t; got: %d, %t\n", cond.want.root, cond.want.hasRoot, got, prs)
			}
		})
	}
}

func TestFindMedian(t *testing.T) {

	// One item in min-heap 0 in max-heap
	oneMinHeap := []heap{
		heap{Type: "min", xi: []int{0, 6}},
		heap{Type: "max", xi: []int{0}},
	}
	// One item in max-heap 0 in min-heap
	oneMaxHeap := []heap{
		heap{Type: "min", xi: []int{0}},
		heap{Type: "max", xi: []int{0, -10}},
	}
	// Even number of items in both min and max-heaps
	evenHeaps := []heap{
		heap{Type: "min", xi: []int{0, 6, 7}},
		heap{Type: "max", xi: []int{0, -10, -9}},
	}

	tests := map[string]struct {
		input []heap
		want  int
	}{
		"1-value min-heap": {oneMinHeap, 6},
		"1-value max-heap": {oneMaxHeap, 10},
		"even heaps":       {evenHeaps, 6},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			got := findMedian(&cond.input[0], &cond.input[1])
			if got != cond.want {
				t.Fatalf("expected: %d, got: %d\n", cond.want, got)
			}
		})
	}
}

func TestBubbleUp(t *testing.T) {
	minHeap := heap{Type: "min", xi: []int{0, 10, 9, 8, 7, 6}}
	maxHeap := heap{Type: "max", xi: []int{0, -1, -2, -3, -4, -5}}

	tests := map[string]struct {
		input heap
		want  heap
	}{
		"min-heap bubble up": {minHeap, heap{"min", []int{0, 6, 10, 8, 7, 9}}},
		"max-heap bubble up": {maxHeap, heap{"max", []int{0, -5, -1, -3, -4, -2}}},
	}

	for name, cond := range tests {
		t.Run(name, func(t *testing.T) {
			cond.input.bubbleUp(5)
			for i, got := range cond.input.xi {
				if got != cond.want.xi[i] {
					t.Fatalf("at index position %d after bubbleUp expected: %d, got: %d\n", i, cond.want.xi[i], got)
				}
			}
		})
	}
}

// func TestInsert(t *testing.T) {}

// func TestLeftIndex(t *testing.T) {}

// func TestRightIndex(t *testing.T) {}

// func TestBubbleDown(t *testing.T) {}

// func TestExtractRoot(t *testing.T) {}
