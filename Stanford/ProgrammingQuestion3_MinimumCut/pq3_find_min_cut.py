# pq3_find_min_cut.py
"""
From Stanford Lagunita Courseware Algorithms: Design and Analysis, 
Part 1, Programming Assignment 3.

The kagerMinCut.txt file contains the adjacency list representation of
a simple undirected graph. There are 200 vertices labeled 1 to 200. The
first column in the file represents the vertex label, and the 
particular row (other entries except the first column) tells all the 
vertices that the vertex is adjacent to. So for example, the row looks
like : "6 155 56 52 120 ......". This just means that the vertex with 
label 6 is adjacent to (i.e., shares an edge with) the vertices with 
labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm
for the min cut problem and use it on the above graph to compute the 
min cut. (HINT: Note that you'll have to figure out an implementation 
of edge contractions. Initially, you might want to do this naively, 
creating a new graph from the old every time there's an edge 
contraction. But you should also think about more efficient 
implementations.) (WARNING: As per the video lectures, please make sure
to run the algorithm many times with different random seeds, and 
remember the smallest cut that you ever find.)
"""

import math
import numpy as np
import random
from collections import defaultdict

def main():
    print("Setting the problem up.")
    vertices, edges, edge_endpoints, node_edges = setup()

    # To ensure we get the correct answer we have to run a 
    # statistically significant number of tests.
    num_runs = len(vertices) * int(math.log2(len(vertices)))

    # Choose an arbitrarily high number to compare against
    min_cuts = np.Infinity
    for i in range(num_runs):
        num_cuts = find_min_cut(vertices, edges, node_edges)
        if num_cuts < min_cuts:
            min_cuts = num_cuts

    print("The minimum number of cuts is {}".format(min_cuts))

def setup():
    """
    Converts the kargerMinCut.txt file into a useable format.
    """

    vertices = []
    edges = []
    node_edges = defaultdict(list)

    with open("kargerMinCut.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            # Remove the trailing tab and newline characters.
            # Otherwise, there are issues on the import.
            line = line.rstrip('\t\n')

            # Build the vertices list.
            vertex = int(line.split('\t', 1)[0])
            vertices.append(vertex)
        
            # edges (relationships) is a list of tuples with the edge 
            # between two points, u and v, represented by a 
            # tuple, (u, v).
            for v in line.split('\t'):
                v = int(v)
                # We don't want self-loops, that is, (1, 1).
                if v != vertex:
                    edge = (vertex, v)
                    edges.append(edge)
                    node_edges[vertex].append(v)

    edge_endpoints = 1

    return vertices, edges, edge_endpoints, node_edges

def find_min_cut(vertices, edges, node_edges):
    """Karger random contraction algorithm."""

    len_vertices = len(vertices)
    while len_vertices > 2:
        # Select an edge (u, v) uniformly at random to remove.
        edge_index = random.randint(0, len_vertices-1)
        u, v = edges[edge_index]
        print("u =", u)
        print("v =", v)

        # Slice out the selected index so it cannot be selected again
        # from edges
        if edge_index+1 < len(edges):
            edges = edges[:edge_index] + edges[edge_index+1:]
        else:
            edges = edges[:-1]

        # Going to have to implement a method to merge edges and remove edges referencing the merged node.

        # Merge the two nodes associated with the edge into a single
        # vertex.
        node_edges[u].append(node_edges.pop(v))
        # Remove references to the merged node, v, within u, as well as
        # self-loops.
        for value in node_edges[u]:
            if value == v or value == u:
                node_edges[u].remove(value)
        # Replace all values of the merged node, v, with u.
        for k, values_list in node_edges.items():
            for value in values_list:
                if value == v:
                    value = u

        vertices.remove(v)

    return len(node_edges.values()[0])

if __name__ == "__main__":
    main()