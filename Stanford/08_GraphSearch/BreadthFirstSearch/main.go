package main

/*
A demonstration program of the breadth first search (BFS) of an
undirected graph to demonstrate BFS's shortest path capabilities.
*/

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("This program demonstrates the shortest path characteristics of breadth first search (BFS) on an undirected graph.")

	nodeEdges := setup()

	startingNode := getNodeValue("start", len(nodeEdges))
	endingNode := getNodeValue("end", len(nodeEdges))

	shortestPath := breadthFirstSearch(startingNode, endingNode, nodeEdges)

	output := generateOutput(shortestPath, startingNode, endingNode)
	fmt.Println(output)
}

func setup() map[int][]int {
	// Converts the kargerMinCut.txt file into a useable format.

	file, err := os.Open("kargerMinCut.txt")
	defer file.Close()
	if err != nil {
		fmt.Println(err)
		return nil
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	m := make(map[int][]int)

	for _, line := range lines {
		xLine := strings.Split(line, "\t")
		// The last tab character leaves a zero value in the slice.
		// Remove it.
		xLine = xLine[0 : len(xLine)-1]
		v := make([]int, len(xLine))
		for idx, value := range xLine {
			val, _ := strconv.Atoi(value)
			v[idx] = val
		}
		m[v[0]] = v[1:]
	}

	return m
}

func getNodeValue(node string, numNodes int) int {
	// Gets user input to designate a starting or ending node.

	inputError := errors.New("Sentinel Error")
	var nodeValue int64

	for inputError != nil {

		if node == "start" {
			fmt.Printf("\nPlease enter your starting node choice (whole number between 1 and %d):\n", numNodes)
		} else {
			fmt.Printf("\nPlease enter your ending node choice (whole number between 1 and %d):\n", numNodes)
		}
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		userInput := fmt.Sprint(scanner.Text())
		nodeValue, inputError = strconv.ParseInt(userInput, 10, 32)
		if (nodeValue < 1 || nodeValue > int64(numNodes)) && inputError == nil {
			inputError = errors.New("input outside of bounds")
		}
		if inputError != nil {
			fmt.Println(inputError)
			fmt.Printf("You have to enter a whole number between 1 and %d!\n", numNodes)
		}
	}

	return int(nodeValue)
}

func breadthFirstSearch(startingNode, endingNode int, nodeEdges map[int][]int) int {
	// Function to explore the given graph for a connection between the
	// starting node and the ending node and return the shortest path
	// between the two nodes if one exists.

	var shortestPath int

	// Short circuit if startingNode == endingNode.
	if startingNode == endingNode {
		return shortestPath
	}

	// Set all the nodes as unexplored.
	isExplored := make(map[int]bool)
	for key := range nodeEdges {
		isExplored[key] = false
	}

	// Set the startingNode as explored.
	isExplored[startingNode] = true

	// Let q = queue data structure (First-in, First-out (FIFO)),
	// initialized with startingNode.
	q := []int{startingNode}

	// dist is a key-value pair representing how many edges we've
	// traversed from startingNode.
	dist := make(map[int]int)
	dist[startingNode] = 0

	for len(q) != 0 {
		// Slice off the first element "pop", since Go does not have
		// built-in push/pop
		u := q[0]
		if len(q) < 2 {
			q = nil
		} else {
			q = q[1:]
		}

		// Explore the different edges u posseses, (u, v).
		for _, v := range nodeEdges[u] {
			if !isExplored[v] {
				dist[v] = dist[u] + 1
				isExplored[v] = true
				q = append(q, v)
			}
		}
	}

	if isExplored[endingNode] {
		shortestPath = dist[endingNode]
	} else {
		// The two nodes are not connected.
		shortestPath = -1
	}
	return shortestPath
}

func generateOutput(pathLength, startingNode, endingNode int) string {
	// Generates the message to the user detailing the result of the
	// breadth first search to find the shortest path.

	var outputMessage string

	if pathLength < 0 {
		outputMessage = fmt.Sprintf("Nodes %d and %d are not connected.\n",
			startingNode, endingNode)
	} else if pathLength == 0 {
		outputMessage = fmt.Sprintln("The shorest path is 0. If you're at home, you don't have to cross the street to get home!")
	} else {
		outputMessage = fmt.Sprintf("The shortest path between nodes %d and %d is %d.\n", startingNode, endingNode, pathLength)
	}

	return outputMessage
}
