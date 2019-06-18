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

from collections import defaultdict

class Node:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

def main():

    # Get all the nodes put into an array
    # Run a BFS from node 1 to find connected nodes and have those 
    # nodes put in an exploration array
    # Have an array storing the distance from 1 to an explored node
    # Return the distances for the nodes requested.
    setup()

    # Breadth-first search to eliminate nodes not connected to source
    # If node not connected to source distance = 1000000
    
    # Return the distance from node 1 to the following ten vertices, in
    # order: 7, 37, 59, 82, 99, 115, 165, 188, 197
    distance_to_node = [7, 37, 59, 82, 99, 115, 165, 188, 197]
    output(distance_to_node)

def find_shortest_paths(source_node, connected_nodes):
    """
    Finds the shortest paths for all nodes connected to the source node.
    """

    explored = [1]

    for idx, _ in enumerate(connected_nodes):
        # Want connections that have been explored as tail and those 
        # nodes that have not yet been explored as head
        
        unexplored = connected_nodes[idx:]
        shortest_path_length = 1000000
        shortest_edge = (0, 0)

        for v_star in explored:
            for w_star in unexplored:
                if w_star in v_star.connections:
                    path_length = find_path_length(v_star, w_star)
                    if path_length < shortest_path_length:
                        shortest_path_length = path_length
                        shortest_edge = (v_star, w_star)
            explored.append(shortest_edge[1])


def find_path_length():
    """
    Finds the shortest path between two nodes
    """

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
            node_edges[source_node]
            
def output(nodes_in_question):
    """
    Prints the distance from the source node to the node in question.
    """

    for node in nodes_in_question:
        print("From node 1 to node {}, the distance is: {}.".format(node, distance))

if __name__ == "__main__":
    main()