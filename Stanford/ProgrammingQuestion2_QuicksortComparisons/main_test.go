package main

import (
	"testing"
)

func TestSetup(t *testing.T) {
	// Check to see if the last value is an int and the correct
	// value from the file
	var got, expected interface{}

	expected = 9269
	xint := setup()
	got = xint[len(xint)-1]

	if got != 9269 {
		t.Errorf("Expected: %v, got: %v.", expected, got)
	} else if got.(int) != expected.(int) {
		t.Errorf("Expected type: %T, got type: %T.", expected, got)
	}
}

func TestSwap(t *testing.T) {
	// Check that swap will swap values in a slice

	initialSlice := []int{1, 2}
	expected := []int{2, 1}
	got := swap(initialSlice, 0, 1)

	for idx, value := range got {
		if value != expected[idx] {
			t.Errorf("Expected: %d at index %d, got: %d.", expected[idx], idx, value)
		}
	}
}

func TestSelectionSort(t *testing.T) {
	// Check that selection sort algorithm returns correctly.

	unsortedSlice := []int{2, 3, 1, 1, 4, 4}
	expected := []int{1, 1, 2, 3, 4, 4}
	got := selectionSort(unsortedSlice)

	for idx, value := range got {
		if value != expected[idx] {
			t.Errorf("Expected: %d at index %d, got: %d.", expected[idx], idx, value)
		}
	}
}

func TestSelectPivot(t *testing.T) {
	// Check selectPivot selects the correct method to choose
	// a pivot index.

	pivotChoices := []string{"first", "last", "median"}
	xint := []int{2, 8, 4, 0}

	expected := []int{0, 3, 0}
	got := make([]int, 3)

	for idx, choice := range pivotChoices {
		got[idx] = selectPivot(xint, 0, len(xint)-1, choice)
	}

	for idx, value := range got {
		if value != expected[idx] {
			t.Errorf("Expected: %d at index %d, got: %d using %v.", expected[idx], idx, value, pivotChoices[idx])
		}
	}
}

func TestSelectPivotMedianOddLengthList(t *testing.T) {
	// Check selectPivot will select the correct median using the "median of
	// three" technique in an odd length list. Even length tested in
	// TestSelectPivot.

	xint := []int{8, 2, 4, 5, 7, 6}

	// Expected value is the index of the pivot selected.
	expected := 3
	got := selectPivot(xint, 1, len(xint)-1, "median")

	if got != expected {
		t.Errorf("Expected median at index %d, got %d.", expected, got)
	}
}

func TestSelectPivotMedianShortLengthList(t *testing.T) {
	// Check that selectPivot will select the correct median using the "median
	// of three" technique in a list of length two.

	xint := []int{1, 2}

	// Expected value is the index of the pivot selected.
	expected := 0
	got := selectPivot(xint, 0, len(xint)-1, "median")

	if got != expected {
		t.Errorf("Expected median at index %d, got %d.", expected, got)
	}
}

func TestQuicksortSortList(t *testing.T) {
	// Test that the quicksort function returns a sorted list.

	unsortedSlice := []int{9, 4, 6, 1, 3, 7, 5, 2, 8, 0}

	expected := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	got, _ := quicksort(unsortedSlice, 0, len(unsortedSlice)-1, "median")

	for idx, value := range got {
		if value != expected[idx] {
			t.Errorf("Expected %d at index %d, got %d", expected[idx], idx, value)
		}
	}
}

func TestQuicksortComparisonsFirst(t *testing.T) {
	// Ensure quicksort returns the correct number of comparisons when
	// the pivot selection method only selects the first element as
	// the pivot.

	unsortedSlice := []int{2, 0, 1, 4, 3}

	expected := 6
	_, got := quicksort(unsortedSlice, 0, len(unsortedSlice)-1, "first")

	if got != expected {
		t.Errorf("Expected %d comparisons, got %d.", expected, got)
	}
}

func TestQuicksortComparisonsLast(t *testing.T) {
	// Ensure quicksort returns the correct number of comparisons when
	// the pivot selection method only selects the last element as
	// the pivot.

	unsortedSlice := []int{8, 5, 0, 1}

	expected := 4
	_, got := quicksort(unsortedSlice, 0, len(unsortedSlice)-1, "last")

	if got != expected {
		t.Errorf("Expected %d comparisons, got %d.", expected, got)
	}
}

func TestQuicksortComparisonsMedian(t *testing.T) {
	// Ensure quicksort returns the correct number of comparisons when
	// the pivot selection method uses the "median of three" to select
	// the pivot element.

	unsortedSlice := []int{8, 2, 4, 5, 7, 1}

	expected := 8
	_, got := quicksort(unsortedSlice, 0, len(unsortedSlice)-1, "median")

	if got != expected {
		t.Errorf("Expected %d comparisons, got %d.", expected, got)
	}
}

func TestQuicksortRepeatedValues(t *testing.T) {
	// Test that the quicksort function returns a sorted list.

	unsortedSlice := []int{9, 4, 6, 1, 8, 3, 7, 5, 2, 8, 0}

	expected := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9}

	got, _ := quicksort(unsortedSlice, 0, len(unsortedSlice)-1, "median")

	for idx, value := range got {
		if value != expected[idx] {
			t.Errorf("Expected %d at index %d, got %d", expected[idx], idx, value)
		}
	}
}
