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

func TestInsert(t *testing.T) {

	type input struct {
		num int
		h   heap
	}

	minInput1 := input{1, heap{Type: "min", xi: []int{0}}}
	maxInput1 := input{1, heap{Type: "max", xi: []int{0}}}
	minInput2 := input{2, heap{Type: "min", xi: []int{0, 1}}}
	maxInput2 := input{0, heap{Type: "max", xi: []int{0, -1}}}
	minInput3 := input{0, heap{Type: "min", xi: []int{0, 1, 2}}}
	maxInput3 := input{3, heap{Type: "max", xi: []int{0, 0, -1}}}

	tests := map[string]struct {
		input
		want heap
	}{
		"min-heap insert to new heap":   {minInput1, heap{Type: "min", xi: []int{0, 1}}},
		"max-heap insert to new heap":   {maxInput1, heap{Type: "max", xi: []int{0, -1}}},
		"min-heap insert larger input":  {minInput2, heap{Type: "min", xi: []int{0, 1, 2}}},
		"max-heap insert smaller input": {maxInput2, heap{Type: "max", xi: []int{0, -1, 0}}},
		"min-heap insert new min input": {minInput3, heap{Type: "min", xi: []int{0, 0, 2, 1}}},
		"max-heap insert new max input": {maxInput3, heap{Type: "max", xi: []int{0, -3, -1, 0}}},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			tc.h.insert(tc.num)
			for i, got := range tc.input.h.xi {
				if got != tc.want.xi[i] {
					t.Fatalf("at index position %d after insert() expected: %d, got: %d\n", i, tc.want.xi[i], got)
				}
			}
		})
	}
}

func TestLeftIndex(t *testing.T) {

	type want struct {
		index  int
		exists bool
	}

	h := heap{Type: "min", xi: []int{0, 1, 2, 3, 4, 5}}

	tests := map[string]struct {
		input int
		want
	}{
		"has left child": {2, want{4, true}},
		"no left child":  {4, want{0, false}},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			got, prs := h.leftIndex(tc.input)
			if got != tc.index || prs != tc.exists {
				t.Fatalf("Expected: %d, %t; Got: %d, %t", tc.index, tc.exists, got, prs)
			}
		})
	}
}

func TestRightIndex(t *testing.T) {

	type want struct {
		index  int
		exists bool
	}

	h := heap{Type: "max", xi: []int{0, 10, 9, 8, 7, 6}}

	tests := map[string]struct {
		input int
		want
	}{
		"has right child": {2, want{5, true}},
		"no right child":  {4, want{0, false}},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			got, prs := h.rightIndex(tc.input)
			if got != tc.index || prs != tc.exists {
				t.Fatalf("Expected: %d, %t; Got: %d, %t", tc.index, tc.exists, got, prs)
			}
		})
	}
}

func TestBubbleDown(t *testing.T) {

	type input struct {
		index int
		h     heap
	}

	minHeap := input{1, heap{Type: "min", xi: []int{0, 10, 2, 3, 4, 5}}}
	maxHeap := input{1, heap{Type: "max", xi: []int{0, -1, -5, -4, -3, -2}}}

	tests := map[string]struct {
		input
		want heap
	}{
		"min-heap bubbledown": {minHeap, heap{Type: "min", xi: []int{0, 2, 4, 3, 10, 5}}},
		"max-heap bubbledown": {maxHeap, heap{Type: "max", xi: []int{0, -5, -3, -4, -1, -2}}},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			tc.h.bubbleDown(tc.index)
			for i, got := range tc.h.xi {
				if got != tc.want.xi[i] {
					t.Fatalf("At index position %d - Expected: %d, Got: %d", i, tc.want.xi[i], got)
				}
			}
		})
	}
}

func TestExtractRoot(t *testing.T) {

	type want struct {
		root   int
		exists bool
	}

	tests := map[string]struct {
		h heap
		want
	}{
		"extract from empty heap":      {heap{Type: "min", xi: []int{0}}, want{0, false}},
		"extract from min-heap":        {heap{Type: "min", xi: []int{0, 1, 2, 3, 4, 5}}, want{1, true}},
		"second extract from min-heap": {heap{Type: "min", xi: []int{0, 2, 4, 3, 5}}, want{2, true}},
		"extract from max-heap":        {heap{Type: "max", xi: []int{0, -10, -9, -8, -7, -6}}, want{10, true}},
		"second extract from max-heap": {heap{Type: "max", xi: []int{0, -9, -8, -6, -7}}, want{9, true}},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			got, prs := tc.h.extractRoot()
			if got != tc.want.root || prs != tc.want.exists {
				t.Fatalf("Expected: %d, %t; Got: %d, %t\n", tc.want.root, tc.want.exists, got, prs)
			}
		})
	}
}

func TestRebalance(t *testing.T) {

	twoDiffHeaps := []heap{
		heap{Type: "min", xi: []int{0, 6, 7, 8, 9, 10}},
		heap{Type: "max", xi: []int{0, -5, -4, -3}},
	}
	wantTwoDH := []heap{
		heap{Type: "min", xi: []int{0, 7, 9, 8, 10}},
		heap{Type: "max", xi: []int{0, -6, -5, -3, -4}},
	}

	threeDiffHeaps := []heap{
		heap{Type: "min", xi: []int{0, 6, 7}},
		heap{Type: "max", xi: []int{0, -5, -4, -3, -2, -1, 0}},
	}
	wantThreeDH := []heap{
		heap{Type: "min", xi: []int{0, 4, 5, 6, 7}},
		heap{Type: "max", xi: []int{0, -3, -2, -1, 0}},
	}

	tests := map[string]struct {
		input []heap
		want  []heap
	}{
		"heaps differ by two elements":           {twoDiffHeaps, wantTwoDH},
		"heaps differ by more than two elements": {threeDiffHeaps, wantThreeDH},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			got0, got1 := rebalance(tc.input[0], tc.input[1])
			if len(got0.xi) != len(tc.want[0].xi) {
				t.Fatalf("Expected length heap[0]: %d, Got length: %d\n", len(tc.want[0].xi), len(got0.xi))
			} else if len(got1.xi) != len(tc.want[1].xi) {
				t.Fatalf("Expected length heap[1]: %d, Got length: %d\n", len(tc.want[1].xi), len(got1.xi))
			}
			for i, got := range got0.xi {
				if got != tc.want[0].xi[i] {
					t.Fatalf("At index %d of got0 - Expected: %d, Got %d\n", i, tc.want[0].xi[i], got)
				}
			}
			for i, got := range got1.xi {
				if got != tc.want[1].xi[i] {
					t.Fatalf("At index %d of got1 -Expected: %d, Got %d\n", i, tc.want[1].xi[i], got)
				}
			}
		})
	}

}
