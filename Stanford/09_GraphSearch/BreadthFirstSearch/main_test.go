package main

import (
	"fmt"
	"testing"
)

func TestSetup(t *testing.T) {
	// Test of the setup function by checking if a node gets formatted
	// correctly.

	// Check to see if node 200 returns correctly
	expected := []int{149, 155, 52, 87, 120, 39, 160, 137, 27, 79, 131, 100,
		25, 55, 23, 126, 84, 166, 150, 62, 67, 1, 69, 35}

	got := setup()
	if len(got[200]) != len(expected) {
		t.Errorf("Slices sizes are not equal.\nExpected:\t%v\nGot:\t\t%v", expected, got[200])
	}
	for idx, value := range got[200] {
		if value != expected[idx] {
			t.Errorf("Expected:\t%v\nGot:\t\t%v", expected, got[200])
		}
	}
}

func TestBreadthFirstSearch(t *testing.T) {
	// Test to ensure all paths of breadthFirstSearch are covered.

	expected := []int{2, 0, -1}
	testType := []string{
		"a path exists.",
		"the starting node is the same as the ending node.",
		"no path exists.",
	}

	startingNode := 1
	endingNodes := []int{4, 1, 3}

	nodeEdges := make(map[int][]int)
	nodeEdges[1] = []int{2}
	nodeEdges[2] = []int{1, 4}
	nodeEdges[3] = []int{3}
	nodeEdges[4] = []int{2}

	got := make([]int, len(expected))

	for idx := range expected {
		got[idx] = breadthFirstSearch(startingNode, endingNodes[idx], nodeEdges)
	}

	for idx, val := range got {
		if val != expected[idx] {
			t.Errorf("Path lengths incorrect for test type - %v Expected: %d, Got: %d.",
				testType[idx], expected[idx], val)
		}
	}
}

func TestGenerateOutput(t *testing.T) {
	// Test to ensure all paths of generateOutput are covered.

	shortestPath := []int{-1, 0, 1}
	startingNode := 1
	endingNodes := []int{19, 1, 2}
	testType := []string{
		"Not Connected",
		"Ending Node is the same as the Starting Node",
		"Shortest Path",
	}

	expected := make([]string, 3)
	expected[0] = fmt.Sprintf("Nodes %d and %d are not connected.\n", startingNode, endingNodes[0])
	expected[1] = fmt.Sprintln("The shorest path is 0. If you're at home, you don't have to cross the street to get home!")
	expected[2] = fmt.Sprintf("The shortest path between nodes %d and %d is %d.\n", startingNode, endingNodes[2], shortestPath[2])

	got := make([]string, 3)
	for idx, val := range expected {
		got[idx] = generateOutput(shortestPath[idx], startingNode, endingNodes[idx])
		if got[idx] != val {
			t.Errorf("For test type - %v\nExpected: %v\nGot: \t%v\n", testType[idx], val, got[idx])
		}
	}
}

/*
Attempt to make a testing function that models user input for the
getNodeValue(s string) string function.
*/
// func TestGetNodeValue(t *testing.T) {
// 	mockUserInput := "150"

// 	expected := 150

// 	got := getNodeValue("start")
// 	reader := bufio.NewReader(strings.NewReader(mockUserInput))

// 	if got != expected {
// 		t.Errorf("Expected %d, got %v from getNodeValue(s string) int", expected, got)
// 	}
// }
