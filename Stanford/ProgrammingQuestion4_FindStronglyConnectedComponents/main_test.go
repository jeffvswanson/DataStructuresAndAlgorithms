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
	nodeEdges[1] = []int{3}
	nodeEdges[2] = []int{1}
	nodeEdges[3] = []int{2}
	nodeEdges[4] = []int{1}

	isExplored := make(map[int]bool)
	isExplored[1] = false
	isExplored[2] = false
	isExplored[3] = false
	isExplored[4] = false

	stronglyConnected := make(map[int][]int)
	// topologicalOrder key = finishing order, value = node
	topologicalOrder := make(map[int]int)
	topologicalOrder[1] = 1
	topologicalOrder[2] = 2
	topologicalOrder[3] = 3
	topologicalOrder[4] = 4

	expectedTopologicalOrder := make(map[int]int)
	expectedTopologicalOrder[1] = 2
	expectedTopologicalOrder[2] = 3
	expectedTopologicalOrder[3] = 1
	expectedTopologicalOrder[4] = 4

	var finishingOrder int
	leadNode := 1
	u := topologicalOrder[len(topologicalOrder)]

	// Node 4 should be last in the finishing order
	// Nodes 2 and 3 get explored and return before node 1.
	expected := 4
	got := depthFirstSearch(nodeEdges, stronglyConnected, topologicalOrder, isExplored, u, finishingOrder, leadNode)

	if got != expected {
		t.Errorf("depthFirstSearch error. Expected: %d, Got %d\n", expected, got)
	}
	for key, value := range expectedTopologicalOrder {
		if topologicalOrder[key] != value {
			t.Errorf("expectedTopologicalOrder[%d] = %d, got topologicalOrder[%d] = %d\n", key, value, key, topologicalOrder[key])
		}
	}
}

func TestTopologicalSort(t *testing.T) {
	// Test of strongly connected component return

	// Directed graph has already been reversed and finishOrder
	// determined.
	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2, 4}
	nodeEdges[2] = []int{3}
	nodeEdges[3] = []int{1}
	nodeEdges[4] = []int{4}

	// key = finish order, value = node
	finishOrder := make(map[int]int)
	finishOrder[1] = 2
	finishOrder[2] = 3
	finishOrder[3] = 1
	finishOrder[4] = 4

	isExplored := make(map[int]bool)
	isExplored[1] = false
	isExplored[2] = false
	isExplored[3] = false
	isExplored[4] = false

	maxNode := len(nodeEdges)

	// key = lead node, value = members of strongly connected component
	expectedSCCs := make(map[int][]int)
	expectedSCCs[4] = []int{4}
	expectedSCCs[1] = []int{1, 2, 3}

	_, got := topologicalSort(nodeEdges, maxNode, finishOrder)

	if len(expectedSCCs) != len(got) {
		t.Errorf("len(expectedSCCs) = %d, len(got) = %d\n", len(expectedSCCs), len(got))
		for k := range got {
			t.Errorf("got[%d] = %v\n", k, got[k])
		}
	}

	for key, value := range expectedSCCs {
		for idx, val := range value {
			if got[key][idx] != val {
				t.Errorf("expectedSCCs[%d] = %d, got[%d] = %d\n", key, value, key, got[key][idx])
			}
		}
	}
}

func TestTop5(t *testing.T) {

	expected := []string{"max Connections: [4 3 2]\n", "max Connections: [10 9 8 7 7]\n"}
	got := make([]string, 2)

	stronglyConnectedLessThan5 := make(map[int][]int)
	stronglyConnectedMoreThan5 := make(map[int][]int)

	stronglyConnectedLessThan5[1] = []int{2, 1}
	stronglyConnectedLessThan5[2] = []int{3, 1, 2}
	stronglyConnectedLessThan5[3] = []int{4, 1, 2, 3}

	stronglyConnectedMoreThan5[1] = []int{5, 1, 2, 3, 4}
	stronglyConnectedMoreThan5[2] = []int{6, 1, 2, 3, 4, 5}
	stronglyConnectedMoreThan5[3] = []int{7, 1, 2, 3, 4, 5, 6}
	stronglyConnectedMoreThan5[4] = []int{8, 1, 2, 3, 4, 5, 6, 7}
	stronglyConnectedMoreThan5[5] = []int{9, 1, 2, 3, 4, 5, 6, 7, 8}
	stronglyConnectedMoreThan5[6] = []int{7, 1, 2, 3, 4, 5, 6}
	stronglyConnectedMoreThan5[7] = []int{10, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	maxNode := len(stronglyConnectedMoreThan5[7])

	got[0] = top5(stronglyConnectedLessThan5, maxNode)
	got[1] = top5(stronglyConnectedMoreThan5, maxNode)

	for idx, val := range expected {
		if val != got[idx] {
			t.Errorf("Expected: %v, Got: %v", val, got[idx])
		}
	}
}
