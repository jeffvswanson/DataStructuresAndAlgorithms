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

import copy
import math
import numpy as np
import sys

from collections import defaultdict

def main():
    print("Setting the problem up.")
    vertices, node_edges = setup()

    num_cuts = find_min_cuts(vertices, node_edges)

    print("The minimum number of cuts is {}".format(num_cuts))

def setup():
    """
    Converts the kargerMinCut.txt file into a useable format.
    """

    vertices = []
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
                    node_edges[vertex].append(v)

    return vertices, node_edges

def find_min_cuts(vertices, node_edges):
    """Function to notify user status of the min-cut search."""

    # This function runs very slowly, but should be able to be sped
    # up by focusing on the karger_algorithm. Slow down may be due to
    # the copy of the vertices and node_edges instead of using 
    # pointers.

    # To ensure we get the correct answer we have to run a 
    # statistically significant number of tests.
    num_runs = int(math.pow(len(vertices),2)) * int(math.log2(len(vertices)))

    # Choose an arbitrarily high number to compare against
    min_cuts = np.Infinity
    for i in range(num_runs):
        print("Iteration {} of {}.".format(i, num_runs))
        node_edges_copy = copy.deepcopy(node_edges)
        vertices_copy = vertices.copy()
        num_cuts = karger_algorithm(vertices_copy, node_edges_copy)
        if num_cuts < min_cuts:
            min_cuts = num_cuts
        print("min_cuts = {}, num_cuts = {}\n".format(min_cuts, num_cuts))
        sys.stdout.flush()

    return min_cuts

def karger_algorithm(vertices, node_edges):
    """Karger random contraction algorithm."""

    while len(vertices) > 2:
        # Select an edge (u, v) uniformly at random to remove.
        u = np.random.choice(vertices)
        v = np.random.choice(node_edges[u])
        
        # Merge the two nodes u and v associated with the edge (u, v) 
        # into a single vertex.
        node_edges[u] += node_edges[v]
        del node_edges[v]

        # Remove references to the merged node, v, within u, as well as
        # self-loops.
        while u in node_edges[u]:
            node_edges[u].remove(u)
        while v in node_edges[u]:
            node_edges[u].remove(v)
        # Replace all edges with values of the merged node, v, with u.
        for k, values_list in node_edges.items():
            while v in values_list:
                node_edges[k].append(u)
                node_edges[k].remove(v)

        vertices.remove(v)
    
    return len(next(iter(node_edges.values())))

if __name__ == "__main__":
    main()