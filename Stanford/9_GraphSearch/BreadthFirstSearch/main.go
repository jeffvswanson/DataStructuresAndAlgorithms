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

	startingNode := getNodeValue("start")
	endingNode := getNodeValue("end")

	fmt.Println(startingNode, endingNode)
	fmt.Println(nodeEdges[1])

	// shortestPath := breadthFirstSearch(startingNode, endingNode, vertices, nodeEdges)

	// output := generateOutput(shortestPath, startingNode, endingNode)
	// fmt.Println(output)
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
	// Take each line
	// Split it at the tabs
	// Take the split line
	// Convert the elements of the slice to ints
	// Add the ints to the slice of ints
	// Map the first value in the slice of ints as the key and all following elements as the values.
	for _, line := range lines {
		xLine := strings.Split(line, "\t")
		v := make([]int, len(xLine)-1)
		for _, values := range xLine {
			for _, value := range values {
				value, _ = strconv.Atoi(value)
				v = append(v, value)
			}
		}
		m[v[0]] = v[1:]
	}

	return m
}

func getNodeValue(node string) int {
	// Gets user input to designate a starting or ending node.

	inputError := errors.New("Sentinel Error")
	var nodeValue int64

	for inputError != nil {

		if node == "start" {
			fmt.Println("\nPlease enter your starting node choice (whole number between 1 and 200): ")
		} else {
			fmt.Println("\nPlease enter your ending node choice (whole number between 1 and 200): ")
		}
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		userInput := fmt.Sprint(scanner.Text())
		nodeValue, inputError = strconv.ParseInt(userInput, 10, 32)
		if (nodeValue < 1 || nodeValue > 200) && inputError == nil {
			inputError = errors.New("input outside of bounds")
		}
		if inputError != nil {
			fmt.Println(inputError)
			fmt.Println("You have to enter a whole number between 1 and 200!")
		}
	}

	return int(nodeValue)
}

// func breadthFirstSearch(startingNode, endingNode int, vertices []int, nodeEdges map[int][]int) int {
//	// Function to explore the given graph for a connection between the
//	// starting node and the ending node and return the shortest path
//	// between the two nodes if one exists.

// }

func generateOutput(pathLength, startingNode, endingNode int) string {
	return "Hello"
}
