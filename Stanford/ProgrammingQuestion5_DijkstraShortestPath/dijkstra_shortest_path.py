# dijktstra_shortest_path.py
"""
An implementation of Dijktra's shortest-path algorithm.

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
"""

from collections import Counter
from collections import defaultdict

class Node:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

def main():

    # nodes put in an exploration array
    # Have an array storing the distance from 1 to an explored node
    # Return the distances for the nodes requested.
    source_node = 1
    graph = setup()

    # Breadth-first search to eliminate nodes not connected to source
    # If node not connected to source distance = 1000000
    connected_to_source = breadth_first_search(graph, source_node)
    for node in graph.keys():
        if node in connected_to_source:
            continue
        else:
            graph[source_node].append((node, 1000000))

    distance_to_source = find_shortest_path(graph, source_node)
    
    # Return the distance from node 1 to the following ten vertices, in
    # order: 7, 37, 59, 82, 99, 115, 165, 188, 197
    distance_to_node = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    output(distance_to_node, distance_to_source)

def setup():
    """
    Converts dijkstraData.txt into a python useable format.
    """

    node_edges = defaultdict(list)

    with open("dijkstraData.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            # Remove the trailing tab and newline characters.
            # Otherwise, there are issues on import.
            line = line.rstrip('\t\n')
            line = line.split('\t')

            source_node = int(line[0])

            for val in line[1:]:
                node_edge = val.split(',')
                node_edges[source_node].append((int(node_edge[0]), int(node_edge[1])))

    return node_edges

def breadth_first_search(graph, source_node):
    """
    Conducts a breadth-first search to determine connections to the
    source node.
    """

    # Set all nodes as unexplored.
    nodes = defaultdict(list)
    # Set the source node as explored
    nodes["Explored"].append(source_node)

    # Let q = queue data structure (First-in, First-out (FIFO))
    # initialized with the source node.
    q = [source_node]

    while len(q) != 0:
        v = q.pop(0)
        # Explore the different edges v possesses (v, w)
        for connection in graph[v]:
            w = connection[0]
            if w in nodes["Explored"]:
                continue
            else:
                nodes["Explored"].append(w)
                q.append(w)

    return nodes["Explored"]

def find_shortest_path(graph, source_node):
    """
    Finds the shortest path between two nodes using Dijkstra's shortest
    path algorithm.
    """

    # Shortest distance to source node is 0.
    distances_to_node = [None] * len(graph)
    distances_to_node[0] = 0
    
    list_of_vertices_processed = [source_node]

    while Counter(list_of_vertices_processed) != Counter(graph.keys()):
        # (source_node, ending_node, distance)
        shortest_path = (source_node, source_node, 10000000) # Use arbitrarily large number
        for v_star in list_of_vertices_processed:
            for w_star in graph[v_star]:
                if w_star[0] in list_of_vertices_processed:
                    continue
                else:                    
                    path_length = distances_to_node[v_star-1] + w_star[1]
                    if path_length < shortest_path[2]:
                        shortest_path = (source_node, w_star[0], path_length)
        if shortest_path[1] != source_node:
            list_of_vertices_processed.append(shortest_path[1])
            distances_to_node[shortest_path[1]-1] = shortest_path[2]

    return distances_to_node

def output(nodes_in_question, distances):
    """
    Prints the distance from the source node to the node in question.
    """
    
    for node in nodes_in_question:
        print("From node 1 to node {} the distance is: {}.".format(node, distances[node-1]))

if __name__ == "__main__":
    main()