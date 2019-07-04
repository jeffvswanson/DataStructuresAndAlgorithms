package main

import "testing"

func TestSetup(t *testing.T) {
	// Expected length of the target values set
	expectedLength := 20001

	// First and last values in algo1-programming-2sum.txt
	expectedValues := []int64{68037543430, -60012933873}

	gotValues, gotTargets := setup()

	for _, v := range expectedValues {
		if _, ok := gotValues[int64(v)]; !ok {
			t.Errorf("setup error. Expected: %d in values slice, but not present.\n", v)
		}
	}

	if expectedLength != len(gotTargets) {
		t.Errorf("setup error. Expected target slice length: %d, Got: %d\n", expectedLength, len(gotTargets))
	}
}

func TestTwoSumSearch(t *testing.T) {

	// Create a values set
	values := make(map[int64]bool)
	xValues := []int64{15, -15, 30, -99, 0}
	for _, v := range xValues {
		values[int64(v)] = true
	}

	// Create a targets set
	targets := make(map[int64]bool)
	for i := -15; i < 16; i++ {
		targets[int64(i)] = true
	}

	expected := 3
	got := twoSumSearch(values, targets)
	if expected != got {
		t.Errorf("two sum search error. Expected %d matches, Got: %d\n", expected, got)
	}
}
