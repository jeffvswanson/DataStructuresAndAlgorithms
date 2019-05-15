package main

import "testing"

func TestSetup(t *testing.T) {
	expectedMaxNode := 875714
	expectedNodeMap := make(map[int][]int)
	expectedNodeMap[875714] = []int{542446, 13655, 542447, 13656, 542448, 542449, 542450, 542451, 542452, 13660, 9434, 542453}
	expectedNodeMapLength := len(expectedNodeMap[875714])

	gotMap, gotOrderMap, gotMaxNode := setup("SCC.txt")
	gotMapLength := len(gotMap[875714])
	gotOrderMapLength := len(gotOrderMap)

	if gotMaxNode != expectedMaxNode {
		t.Errorf("Setup error. Expected max node of: %d, Got %d\n", expectedMaxNode, gotMaxNode)
	}
	if gotMapLength != expectedNodeMapLength || gotOrderMapLength != expectedMaxNode {
		t.Errorf("Setup failure. Expected len(nodeEdges[875714]) = %d, Got: %d\n", expectedNodeMapLength, gotMapLength)
	}
	if gotOrderMap[expectedMaxNode] != expectedMaxNode {
		t.Errorf("Setup failure. Expected gotOrderMapLength[%d] = %d, Got: %d\n", expectedMaxNode, expectedMaxNode, gotOrderMap[gotOrderMapLength])
	}
	for idx, val := range gotMap[875714] {
		if val != expectedNodeMap[875714][idx] {
			t.Errorf("Setup failure.\nExpected: %v\nGot: %v\n", expectedNodeMap[875714], gotMap[875714])
		}
	}
}

func TestReverseGraph(t *testing.T) {
	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2, 3}
	nodeEdges[2] = []int{3}
	nodeEdges[3] = []int{1}

	expected := make(map[int][]int)
	expected[1] = []int{3}
	expected[2] = []int{1}
	expected[3] = []int{1, 2}

	got := reverseGraph(nodeEdges)
	for key, value := range expected {
		for idx, val := range value {
			if val != got[key][idx] {
				t.Errorf("Expected: %v, Got: %v at Key: %v, Index position: %v\n", val, got[key][idx], key, idx)
			}
		}
	}
}

func TestDepthFirstSearch(t *testing.T) {
	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2, 3}
	nodeEdges[2] = []int{3}
	nodeEdges[3] = []int{1}

	isExplored := make(map[int]bool)
	isExplored[1] = false
	isExplored[2] = false
	isExplored[3] = false

	stronglyConnected := make(map[int][]int)
	topologicalOrder := make(map[int]int)

	var finishingOrder int
	leadNode := 1
	u := 1

	// Node 1 should be last in the finishing order
	// Nodes 2 and 3 get explored and return before node 1.
	expected := 3
	got := depthFirstSearch(nodeEdges, stronglyConnected, topologicalOrder, isExplored, u, finishingOrder, leadNode)

	if got != expected {
		t.Errorf("depthFirstSearch error. Expected: %d, Got %d\n", expected, got)
	}
}

func TestTopologicalSort(t *testing.T) {
	// Test of strongly connected component return

	// Directed graph has already been reversed and finishOrder
	// determined.
	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2, 3}
	nodeEdges[2] = []int{3}
	nodeEdges[3] = []int{1}

	finishOrder := make(map[int]int)
	finishOrder[1] = 1
	finishOrder[2] = 2
	finishOrder[3] = 3

	isExplored := make(map[int]bool)
	isExplored[1] = false
	isExplored[2] = false
	isExplored[3] = false

	maxNode := len(nodeEdges)

	expected := []int{3, 1, 2}
	expectedLength := 1

	_, got := topologicalSort(nodeEdges, maxNode, finishOrder)

	if expectedLength != len(got) {
		t.Errorf("len(expected) = %d, len(got) = %d\n", len(expected), len(got))
		for k := range got {
			t.Errorf("got[%d] = %v\n", k, got[k])
		}
	}

	for idx, val := range expected {
		if val != got[3][idx] {
			t.Errorf("Expected: %v, Got: %v at Key: %v, Index position: %v\n", val, got[1][idx], 1, idx)
		}
	}
}
