package main

import (
	"reflect"
	"testing"
)

func TestSetup(t *testing.T) {

	expected := make(map[int][]connection)
	expected[1] = []connection{
		{80, 982},
		{163, 8164},
		{170, 2620},
		{145, 648},
		{200, 8021},
		{173, 2069},
		{92, 647},
		{26, 4122},
		{140, 546},
		{11, 1913},
		{160, 6461},
		{27, 7905},
		{40, 9047},
		{150, 2183},
		{61, 9146},
		{159, 7420},
		{198, 1724},
		{114, 508},
		{104, 6647},
		{30, 4612},
		{99, 2367},
		{138, 7896},
		{169, 8700},
		{49, 2437},
		{125, 2909},
		{117, 2597},
		{55, 6399},
	}

	got := setup()
	if len(got) < 200 {
		t.Errorf("data import error. Expected: %d, Got: %d\n", 200, len(got))
	}
	if !reflect.DeepEqual(expected[1], got[1]) {
		t.Errorf("data import error. Expected:\n%v\nGot:\n%v\n", expected[1], got[1])
	}
}

func TestBreadthFirstSearch(t *testing.T) {

	source := 1
	input := make(map[int][]connection)
	input[1] = []connection{{2, 4}}
	input[3] = []connection{{2, 4}}

	expected := make(map[int][]connection)
	expected[1] = []connection{{2, 4}}
	got := breadthFirstSearch(input, source)

	if !reflect.DeepEqual(expected, got) {
		t.Errorf("breadth-first search error. Expected: %v, Got: %v\n", expected, got)
	}
}

func TestFindShortestPath(t *testing.T) {

	input := make(map[int][]connection)
	input[1] = []connection{{2, 3}, {3, 4}, {4, 5}, {5, 6}}
	input[2] = []connection{{3, 3}, {4, 1}}
	input[3] = []connection{{5, 1}}
	input[4] = []connection{{5, 3}}
	input[5] = []connection{{2, 3}}
	source := 1

	expected := []int{0, 3, 4, 4, 5}

	got := findShortestPath(input, source)

	if len(got) != len(expected) {
		t.Errorf("findShortestPath error. Expected length: %d, Got: %d\n", len(expected), len(got))
	}
	for idx, val := range expected {
		if val != got[idx] {
			t.Errorf("findShortestPath failure. At index %d - Expected: %d, Got: %d\n", idx, val, got[idx])
		}
	}
}

func TestGenOutput(t *testing.T) {

	expected := []int{0, 10}
	nodes := []int{1, 2}
	distance := []int{0, 10}

	got := genOutput(nodes, distance)

	if len(got) != len(expected) {
		t.Errorf("genOutput error. Expected length: %d, Got: %d\n", len(expected), len(got))
	}
	for idx, val := range expected {
		if val != got[idx] {
			t.Errorf("genOutput failure. At index %d - Expected: %d, Got: %d\n", idx, val, got[idx])
		}
	}
}
