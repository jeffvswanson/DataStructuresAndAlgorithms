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
	"sort"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("This program demonstrates Kosaraju's Two-Pass algorithm on a directed graph.")

	nodeEdges, initFinishOrder, maxNode := setup("SCC.txt")

	// Step 1: Given a directed graph, reverse the graph.
	// That is, a --> b becomes a <-- b.
	reversedNodeEdges := reverseGraph(nodeEdges)

	// Step 2, Pass 1: Run a topological sort using the reversed graph.
	// This step gives the order to search nodes in the next step.
	finishOrder, _ := topologicalSort(reversedNodeEdges, maxNode, initFinishOrder)

	// Step 3, Pass 2: Run a topological sort with the original graph.
	// This step discovers the SCCs.
	_, stronglyConnected := topologicalSort(nodeEdges, maxNode, finishOrder)

	output := top5(stronglyConnected, maxNode)
	fmt.Print(output)
}

func setup(fileName string) (map[int][]int, map[int]int, int) {
	// converts the SCC.txt file into a Go useable format.

	file, err := os.Open(fileName)
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return nil, nil, 0
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

	// Some nodes are only tails and must be accounted for.
	ascendingFinishOrder := make(map[int]int)

	for node := 1; node <= maxNode; node++ {
		ascendingFinishOrder[node] = node
		if _, head := nodeEdges[node]; !head {
			nodeEdges[node] = []int{node}
		}
	}

	return nodeEdges, ascendingFinishOrder, maxNode
}

func reverseGraph(originalGraph map[int][]int) map[int][]int {
	// Reverses node relationships in a graph.

	reversedGraph := make(map[int][]int)

	for head, tails := range originalGraph {
		for _, tail := range tails {
			reversedGraph[tail] = append(reversedGraph[tail], head)
		}
	}

	// Some nodes are only sources in the original graph and will not
	// be represented in the reversed graph if they do not have self-
	// references.
	for node := 1; node <= len(originalGraph); node++ {
		if _, ok := reversedGraph[node]; !ok {
			reversedGraph[node] = []int{node}
		}
	}

	return reversedGraph
}

func topologicalSort(nodeEdges map[int][]int, maxNode int, finishOrder map[int]int) (map[int]int, map[int][]int) {
	// Outer loop for depth first search to keep track of a vertex's
	// order of finishing, that is, when the inner loop,
	// depthFirstSearch(), cannot recurse any further.

	// Mark all nodes as unexplored.
	isExplored := make(map[int]bool)
	for node := 1; node <= len(nodeEdges); node++ {
		isExplored[node] = false
	}

	// finishingOrder, a lower value means the node processed first
	var finishingOrder, leadNode int
	stronglyConnected := make(map[int][]int)

	// Have to make a true copy without changing the original map.
	finishOrderCopy := make(map[int]int)
	for key, value := range finishOrder {
		finishOrderCopy[key] = value
	}

	for i := len(finishOrder); i > 0; i-- {
		u := finishOrder[i]
		if !isExplored[u] {
			leadNode = u
			finishingOrder = depthFirstSearch(nodeEdges, stronglyConnected,
				finishOrderCopy, isExplored, u, finishingOrder, leadNode)
		}
	}

	return finishOrderCopy, stronglyConnected
}

func depthFirstSearch(nodeEdges, stronglyConnected map[int][]int,
	finishOrderCopy map[int]int, isExplored map[int]bool, u, finishingOrder,
	leadNode int) int {
	// Depth first search implementation. Searches a directed graph
	// until the search hits an explored node and returns where the
	// node is in relation to other vertices.

	isExplored[u] = true

	stronglyConnected[leadNode] = append(stronglyConnected[leadNode], u)

	for _, v := range nodeEdges[u] {
		if !isExplored[v] {
			finishingOrder = depthFirstSearch(nodeEdges, stronglyConnected,
				finishOrderCopy, isExplored, v, finishingOrder, leadNode)
		}
	}
	finishingOrder++
	finishOrderCopy[finishingOrder] = u

	return finishingOrder
}

func top5(stronglyConnected map[int][]int, maxNode int) string {

	var output string
	maxConnections := make([]int, 0)

	for node := 1; node <= maxNode; node++ {
		if len(stronglyConnected[node]) > 0 {
			maxConnections = append(maxConnections, len(stronglyConnected[node]))
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(maxConnections)))

	if len(maxConnections) < 5 {
		output = fmt.Sprintln("max Connections:", maxConnections)
	} else {
		output = fmt.Sprintln("max Connections:", maxConnections[:5])
	}

	return output
}
