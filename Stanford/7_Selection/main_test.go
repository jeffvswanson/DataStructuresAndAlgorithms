package main

import "testing"

var quickSelectTests = []struct {
	kOrderStat int
	expected   int
}{
	{1, 0},
	{2, 1},
	{3, 2},
	{4, 3},
	{5, 4},
	{6, 5},
	{7, 6},
	{8, 7},
	{9, 8},
	{10, 9},
}

func TestQuickSelect(t *testing.T) {
	data := []int{9, 3, 4, 5, 7, 1, 2, 8, 6, 0}

	for _, tt := range quickSelectTests {
		_, got := quickSelect(data, tt.kOrderStat)
		if got != tt.expected {
			t.Errorf("quickSelect(data, %d), expected: %d, got %d.",
				tt.kOrderStat, tt.expected, got)
		}
	}
}

func TestSwap(t *testing.T) {
	data := []int{1, 2}
	expected := []int{2, 1}
	got := swap(data, 0, 1)

	for idx, val := range got {
		if val != expected[idx] {
			t.Errorf("At index %d, expected: %d, got %d", idx, expected[idx],
				val)
		}
	}
}
