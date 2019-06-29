package main

import (
	"math"
	"testing"
)

func TestGenKOrderStat(t *testing.T) {
	// Test of uniform randomness of genKOrderStat
	// This test can and will fail from time to time because the
	// results are random, however, it should pass more often than not.

	hypotheticalSliceLength := 20
	results := make([]int, hypotheticalSliceLength+1)

	numIterations := 10000
	for i := 0; i < numIterations; i++ {
		k := genKOrderStat(hypotheticalSliceLength)
		if k > 0 && k <= hypotheticalSliceLength+1 {
			results[k]++
		} else {
			t.Errorf("k order statistic value outside of expected range [1, %d]. Got: %d", hypotheticalSliceLength, k)
		}
	}

	expectedCounts := float64(numIterations / hypotheticalSliceLength)
	var chiSquared float64
	for i := 1; i < hypotheticalSliceLength+1; i++ {
		observedCounts := float64(results[i])
		chiSquared += math.Pow(observedCounts-expectedCounts, 2) / expectedCounts
	}

	// significance level = 0.01
	// degrees of freedom = 19
	// critical value, alpha = 36.191
	alpha := 36.191
	if chiSquared > 36.191 {
		t.Errorf("Received chi squared value of %v. Should be less than %v.\n", chiSquared, alpha)
		t.Errorf("results: %v", results)
	}
}
