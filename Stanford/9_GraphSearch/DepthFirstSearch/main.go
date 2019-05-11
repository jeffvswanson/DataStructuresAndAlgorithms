package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("This program demonstrates the topological sort characteristic of depth first search (DFS) on a directed graph.")

	nodeEdges, maxNode := setup("SCC.txt")

	topologicalOrder, sortedKeys := topologicalSort(nodeEdges, maxNode)

	writeToFile(topologicalOrder, sortedKeys)
}

func setup(fileName string) (map[int][]int, int) {
	// converts the SCC.txt file into a Go useable format.

	file, err := os.Open(fileName)
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return nil, 0
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	// For node edges the key will be a node at the tail and the values
	// will be the nodes at the heads of the directed section.
	// So, (a, b) = a --> b and the key would be a with a value of b.
	nodeEdges := make(map[int][]int)
	var maxNode int

	for scanner.Scan() {
		xLine := strings.Split(scanner.Text(), " ")
		// The last space character leaves a zero value in the slice,
		// remove it.
		xLine = xLine[0 : len(xLine)-1]

		v := make([]int, len(xLine))
		for idx, value := range xLine {
			val, _ := strconv.Atoi(value)
			v[idx] = val
		}
		nodeEdges[v[0]] = append(nodeEdges[v[0]], v[1])
		if v[0] > maxNode {
			maxNode = v[0]
		}

	}
	return nodeEdges, maxNode
}

func topologicalSort(nodeEdges map[int][]int, maxNode int) (map[int]int, []int) {
	// Outer loop for depth first search to keep track of a vertex's
	// order of precedence.

	// Mark all nodes as unexplored
	isExplored := make(map[int]bool)
	// Create a slice of sorted keys since Go maps are not ordered.
	// This will help the return of topological order by giving a
	// consistent entry point into the graph.
	sortedKeys := make([]int, maxNode)
	for key := 1; key <= maxNode; key++ {
		isExplored[key] = false
		sortedKeys[key-1] = key
	}

	// precedenceOrder, a larger number means it has lower precedence
	precedenceOrder := maxNode
	topologicalOrder := make(map[int]int)

	for u := range sortedKeys {
		if !isExplored[u] {
			precedenceOrder = depthFirstSearch(nodeEdges, topologicalOrder,
				isExplored, u, precedenceOrder)
		}
	}
	return topologicalOrder, sortedKeys
}

func depthFirstSearch(nodeEdges map[int][]int, topologicalOrder map[int]int, isExplored map[int]bool, u, precedenceOrder int) int {
	// Depth first search implementation. Searches a directed graph
	// until the search hits an explored node and returns where the
	// node is in relation to other vertices.

	isExplored[u] = true

	for v := range nodeEdges[u] {
		if !isExplored[v] {
			precedenceOrder = depthFirstSearch(nodeEdges, topologicalOrder,
				isExplored, v, precedenceOrder)
		}
	}
	topologicalOrder[u] = precedenceOrder
	precedenceOrder--

	return precedenceOrder
}

func writeToFile(topologicalOrder map[int]int, sortedKeys []int) {
	f, err := os.Create("topologicalOrder.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()
	fmt.Printf("sortedKeys[0] = %d\n", sortedKeys[0])
	fmt.Printf("sortedKeys[maxNode] = %d\n", sortedKeys[len(sortedKeys)-1])
	for _, key := range sortedKeys {
		_, err := f.WriteString(fmt.Sprintf("%d\t\t\t%d\n", key, topologicalOrder[key]))
		if err != nil {
			fmt.Println(err)
		}
	}
	f.Sync()
}
