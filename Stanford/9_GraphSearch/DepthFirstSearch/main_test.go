package main

import "testing"

func TestSetup(t *testing.T) {
	expectedMaxNode := 875714
	expectedNodeMap := make(map[int][]int)
	expectedNodeMap[875714] = []int{542446, 13655, 542447, 13656, 542448, 542449, 542450, 542451, 542452, 13660, 9434, 542453}
	expectedNodeMapLength := len(expectedNodeMap[875714])

	gotMap, gotMaxNode := setup("SCC.txt")
	gotMapLength := len(gotMap[875714])

	if gotMaxNode != expectedMaxNode {
		t.Errorf("Setup error. Expected max node of: %d, Got %d\n", expectedMaxNode, gotMaxNode)
	}
	if gotMapLength != expectedNodeMapLength {
		t.Errorf("Setup failure. Expected len(nodeEdges[875714]) = %d, Got: %d\n", expectedNodeMapLength, gotMapLength)
	}
	for idx, val := range gotMap[875714] {
		if val != expectedNodeMap[875714][idx] {
			t.Errorf("Setup failure.\nExpected: %v\nGot: %v\n", expectedNodeMap[875714], gotMap[875714])
		}
	}
}

func TestDepthFirstSearch(t *testing.T) {
	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2, 3}
	nodeEdges[2] = []int{1}
	nodeEdges[3] = []int{1}

	isExplored := make(map[int]bool)
	isExplored[1] = false
	isExplored[2] = false
	isExplored[3] = false

	topologicalOrder := make(map[int]int)

	precedenceOrder := 3

	// Node 1 should be first in the precedence order
	expected := 1
	got := depthFirstSearch(nodeEdges, topologicalOrder, isExplored, 1, precedenceOrder)

	if got != expected {
		t.Errorf("depthFirstSearch error. Expected: %d, Got %d\n", expected, got)
	}
}
