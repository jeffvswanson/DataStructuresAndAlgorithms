# kosarajus_algorithm.py
"""
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

This will not work natively on Windows computers. I was only able to 
get it to work in a Linux Docker container running on Windows. I 
cannot speak to native Linux or Mac implementations. This is due to 
the recursion depth of the problem. On Windows I was able to only get
to a maximum recursion depth of around 3921 plus or minus a few frames
whether the stack size was set to 64 MB or 256 MB. The stack depth
needed for this problem is at least 600329.

The resource library is a Linux only library as well.
"""

import copy
import resource
import sys

from collections import defaultdict

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, 
                                            resource.RLIM_INFINITY))
sys.setrecursionlimit(2 ** 17)

def main():

    print("This program demonstrates Kosaraju's Two-Pass algorithm on a \
directed graph.\n", flush=True)

    node_edges, initial_finish_order, max_node = setup()

    # Step 1: Given a directed graph, reverse the graph.
    # That is, a --> b becomes a <-- b.
    reversed_node_edges = reverse_graph(node_edges)

    # Step 2, Pass 1: Run a topological sort using the reversed graph.
    # This step gives the order to search nodes in the next step.
    finish_order, _ = topological_sort(reversed_node_edges, max_node, 
                                        initial_finish_order)

    # Step 3, Pass 2: Run a topological sort with the original graph.
    # This step discovers the SCCs.
    _, strongly_connected = topological_sort(node_edges, max_node, 
                                            finish_order)

    output = top5(strongly_connected, max_node)
    print(output)

def setup():
    """
    Converts the SCC.txt file into a python useable format.
    """

    # For node_edges the key will be a node at the tail and the values
    # will be the nodes at the heads of the directed section
    # So, (a, b) = a --> b and the key would be a with a value of b. 
    # key = head, value = list of tails
    node_edges = defaultdict(list)
    max_node = 0

    with open("SCC.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            # Remove the trailing space and newline characters.
            # Otherwise, there are issues on import
            line = line.rstrip(' \n')
            line = line.split(' ')

            source_node = int(line[0])            
            node_edges[source_node].append(int(line[1]))
            if source_node > max_node:
                max_node = source_node

    # Some nodes are only tails and must be accounted for.
    # key = finish order, value = node
    ascending_finish_order = defaultdict(int)
    for node in range(1, max_node+1):
        ascending_finish_order[node] = node
        if not (node in node_edges):
            node_edges[node] = [node]

    return node_edges, ascending_finish_order, max_node

def reverse_graph(original_graph):
    """Reverses node relationships in a graph."""

    reversed_graph = defaultdict(list)

    for head, tails in original_graph.items():
        for tail in tails:
            reversed_graph[tail].append(head)

    # Some nodes are only sources in the original graph and will not be
    # represented in the reversed graph if they do not have self-
    # references.
    for node in range(1, len(original_graph)+1):
        if not (node in reversed_graph):
            reversed_graph[node] = [node]

    return reversed_graph

def topological_sort(node_edges, max_node, finish_order):
    """
    Outer loop for depth-first search to keep track of a vertex's order
    of finishing, that is, when the inner loop, depth_first_search(),
    cannot recurse any further.
    """
    
    # Mark all nodes as unexplored
    is_explored = defaultdict(bool)
    for node in range(1, max_node+1):
        is_explored[node] = False
    
    # Keeps track of topological order.
    # finishing_order, a larger number means it finished later.
    finishing_order, lead_node = 0, 0

    # Have to make a deep copy to avoid changing the dictionary.
    finish_order_copy = copy.deepcopy(finish_order)

    # key = lead node, value = list of members in the SCC.
    strongly_connected = defaultdict(list)

    for i in range(len(finish_order), 0, -1):
        u = finish_order[i]
        lead_node = u
        if not is_explored[u]:
            finishing_order, strongly_connected = depth_first_search(node_edges, 
                                                    strongly_connected, 
                                                    finish_order_copy, 
                                                    is_explored, u, 
                                                    finishing_order, lead_node)

    return finish_order_copy, strongly_connected

def depth_first_search(node_edges, strongly_connected, finish_order_copy, 
                        is_explored, u, finishing_order, lead_node):
    """
    Depth first search implementation. Searches a directed graph until
    the search hits an explored node and returns where the node is 
    in relation to the other vertices.
    """

    is_explored[u] = True

    strongly_connected[lead_node].append(u)

    for v in node_edges[u]:
        if not is_explored[v]:
            finishing_order, strongly_connected = depth_first_search(node_edges, 
                                                    strongly_connected, 
                                                    finish_order_copy, 
                                                    is_explored, v, 
                                                    finishing_order, lead_node)

    finishing_order += 1
    finish_order_copy[finishing_order] = u
    
    return finishing_order, strongly_connected

def top5(strongly_connected, max_node):

    max_connections = []
    for node in range(1, max_node+1):
        if len(strongly_connected[node]) > 0:
            max_connections.append(len(strongly_connected[node]))

    max_connections.sort(reverse=True)

    if len(max_connections) < 5:
        output = "max Connections: {}".format(max_connections)
    else:
        output = "max Connections: {}".format(max_connections[:5])

    return output

if __name__ == "__main__":
    main()