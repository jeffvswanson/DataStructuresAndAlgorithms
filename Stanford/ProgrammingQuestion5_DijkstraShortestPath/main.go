/*
An implementation of Dijkstra's shortest-path algorithm.

The file contains an adjacency list representation of an undirected
weighted graph with 200 vertices labeled 1 to 200. Each row consists
of the node tuples that are adjacent to that particular vertex along
with the length of that edge. For example, the 6th row has 6 as the
first entry indicating that this row corresponds to the vertex
labeled 6. The next entry of this row "141,8200" indicates that
there is an edge between vertex 6 and vertex 141 that has length 8200.
The rest of the pairs of this row indicate the other vertices adjacent
to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph,
using 1 (the first vertex) as the source vertex, and to compute the
shortest-path distances between 1 and every other vertex of the graph.
If there is no path between a vertex v and vertex 1, we'll define the
shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten
vertices, in order: 7,37,59,82,99,115,133,165,188,197. Enter the
shortest-path distances using the fields below for each of the
vertices.

IMPLEMENTATION NOTES: This graph is small enough that the
straightforward O(mn) time implementation of Dijkstra's algorithm
should work fine. OPTIONAL: For those of you seeking an additional
challenge, try implementing the heap-based version. Note this
requires a heap that supports deletions, and you'll probably need
to maintain some kind of mapping between vertices and their positions
in the heap.
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type connection struct {
	Sink, Distance int
}

type path struct {
	Head, Tail, Length int
}

func main() {

	sourceNode := 1
	graph := setup()

	// Breadth-first search to eliminate nodes not connected to source.
	// If node nod connected to source distance = 1000000
	connected := breadthFirstSearch(graph, sourceNode)
	for node := range graph {
		if _, ok := connected[node]; !ok {
			graph[sourceNode] = append(graph[sourceNode], connection{node, 1000000})
		}
	}

	distanceToSource := findShortestPath(graph, sourceNode)

	// Return the distance from the source node to the following ten
	// vertices, in order: 7, 37, 59, 82, 99, 115, 165, 188, 197.
	nodesInQuestion := []int{7, 37, 59, 82, 99, 115, 165, 188, 197}
	output := genOutput(nodesInQuestion, distanceToSource)
	for i, v := range output {
		fmt.Printf("The distance to node %d from the source node is %d.\n", nodesInQuestion[i], v)
	}
}

// setup converts dijkstraData.txt into Go useable format.
func setup() map[int][]connection {

	nodeMap := make(map[int][]connection)

	f, err := os.Open("dijkstraData.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		xLine := strings.Split(scanner.Text(), "\t")
		var head int

		for _, val := range xLine {
			// Get rid of the parentheses
			val = strings.TrimFunc(val, func(r rune) bool {
				return !unicode.IsNumber(r)
			})

			splitVal := strings.Split(val, ",")

			var tail, distance int
			if len(splitVal) < 2 && splitVal[0] != "" {
				h, err := strconv.Atoi(splitVal[0])
				if err != nil {
					fmt.Println(err)
				}
				head = h
			} else {
				for index, v := range splitVal {
					if v != "" && index < 1 {
						t, err := strconv.Atoi(v)
						if err != nil {
							fmt.Println(err)
						}
						tail = t
					} else if v != "" && index > 0 {
						d, err := strconv.Atoi(v)
						if err != nil {
							fmt.Println(err)
						}
						distance = d
					}
				}
			}
			node := connection{
				tail,
				distance,
			}
			if node.Sink != 0 {
				nodeMap[head] = append(nodeMap[head], node)
			}
		}
	}
	return nodeMap
}

// breadthFirstSearch explores the given graph for a connection between
// the source node and all other nodes in the graph returning a new
// graph only with nodes connected to the source node.
func breadthFirstSearch(graph map[int][]connection, sourceNode int) map[int][]connection {

	searchedGraph := make(map[int][]connection)
	for k, v := range graph {
		searchedGraph[k] = v
	}

	// Set all nodes as unexplored.
	isExplored := make(map[int]bool)
	for key := range graph {
		isExplored[key] = false
	}
	// Except the starting node.
	isExplored[sourceNode] = true

	// Let q = queue data structure (First-in, First-out (FIFO))
	// initialized with the source node.
	q := []int{sourceNode}

	for len(q) != 0 {
		u := q[0]
		if len(q) < 2 {
			q = nil
		} else {
			q = q[1:]
		}
		// Explore the different edges u possesses, (u, v).
		if _, prs := graph[u]; prs {
			for _, v := range graph[u] {
				if !isExplored[v.Sink] {
					isExplored[v.Sink] = true
					q = append(q, v.Sink)
				}
			}
		}
	}
	for node := range graph {
		if !isExplored[node] {
			delete(searchedGraph, node)
		}
	}
	return searchedGraph
}

// findShortestPath finds the shortest path using Dijkstra's shortest
// path algorithm from the source node to the node in question.
func findShortestPath(graph map[int][]connection, sourceNode int) []int {

	distanceTo := make([]int, len(graph))
	distanceTo[0] = 0

	// Let v be the list of vertices processed so far
	v := make(map[int]struct{})
	v[sourceNode] = struct{}{}

	for len(v) < len(graph) {
		// Use arbitrarily large number
		shortestPath := path{
			Head:   sourceNode,
			Tail:   sourceNode,
			Length: 10000000,
		}
		for vStar := range v {
			for _, wStar := range graph[vStar] {
				if _, prs := v[wStar.Sink]; !prs {
					pathLength := distanceTo[vStar-1] + wStar.Distance
					if pathLength < shortestPath.Length {
						shortestPath = path{
							Head:   sourceNode,
							Tail:   wStar.Sink,
							Length: pathLength,
						}
					}
				}
			}
		}
		if shortestPath.Tail != sourceNode {
			v[shortestPath.Tail] = struct{}{}
			distanceTo[shortestPath.Tail-1] = shortestPath.Length
		}
	}
	return distanceTo
}

// genOutput generates the output strings.
func genOutput(nodes, distance []int) []int {

	answers := make([]int, len(nodes))

	for idx, node := range nodes {
		answers[idx] = distance[node-1]
	}
	return answers
}
