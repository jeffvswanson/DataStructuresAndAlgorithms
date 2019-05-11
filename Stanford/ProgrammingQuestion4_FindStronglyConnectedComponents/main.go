package main

/*
Programming Assignment 4, accessed 10 May 2019, from:
Stanford Online Lagunita, Algorithms: Design and Analysis, Part 1.

The file, SCC.txt, contains the edges of a directed graph. Vertices are
labeled as positive integers from 1 to 875714. Every row indicates an
edge, the vertex label in first column is the tail and the vertex label
in second column is the head (recall the graph is directed, and the
edges are directed from the first column vertex to the second column
vertex). So for example, the 11th row looks liks : "2 47646". This just
means that the vertex with label 2 has an outgoing edge to the vertex
with label 47646.

Your task is to code up the algorithm from the video lectures,
Kosaraju's Two-Pass Algorithm, for computing strongly connected
components (SCCs), and to run this algorithm on the given graph.
*/

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("This program demonstrates Kosaraju's Two-Pass algorithm on a directed graph.")

	nodeEdges, maxNode := setup("SCC.txt")

	// Step 1: Given a directed graph, reverse the graph.
	// That is, a --> b becomes a <-- b.
	reversedNodeEdges := reverseGraph(nodeEdges)

	// Step 2, Pass 1: Run a topological sort using the reversed graph.
	// This step gives an ordering of nodes used in the next step.
	finishOrder, _ := topologicalSort(reversedNodeEdges, maxNode, nil)

	// Step 3, Pass 2: Run a topological sort with the original graph.
	// This step discovers the SCCs.
	stronglyConnected, sortedKeys := topologicalSort(nodeEdges, maxNode, finishOrder)

	writeToFile(stronglyConnected, sortedKeys)
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

func reverseGraph(originalGraph map[int][]int) map[int][]int {
	// Reverses node relationships in a graph.

	reversedGraph := make(map[int][]int)

	for key, value := range originalGraph {
		for _, val := range value {
			reversedGraph[val] = append(reversedGraph[val], key)
		}
	}

	return reversedGraph
}

func topologicalSort(nodeEdges map[int][]int, maxNode int, finishOrder map[int]int) (map[int]int, []int) {
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
	f, err := os.Create("StronglyConnectedComponents.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	for _, key := range sortedKeys {
		_, err := f.WriteString(fmt.Sprintf("%d\t\t\t%d\n", key, topologicalOrder[key]))
		if err != nil {
			fmt.Println(err)
		}
	}
	f.Sync()
}
