# depth_first_search.py
"""Demonstration program of the depth first search (DFS) of a directed
graph to demonstrate DFS's topological sort capabilities.

This will not work natively on Windows computers. I was only able to 
get it to work in a Linux Docker container running on Windows. I 
cannot speak to native Linux or Mac implementations. This is due to 
the recursion depth of the problem. On Windows I was able to only get
to a maximum recursion depth of around 3921 plus or minus a few frames
whether the stack size was set to 64 MB or 256 MB. The stack depth
needed for this problem is at least 600497.

The resource library is a Linux only library as well.
"""

import os
import resource
import sys

from collections import defaultdict

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, 
                                            resource.RLIM_INFINITY))
sys.setrecursionlimit(2 ** 17)

def main():

    print("This program demonstrates the topological sort characteristic \
of depth first search (DFS) on a directed graph.\n", flush=True)

    node_edges = setup()

    topological_order = topological_sort(node_edges)

    location = write_to_file(topological_order)

    print("The file location is located in:", location)

def setup():
    """
    Converts the SCC.txt file into a python useable format.
    """

    # For node_edges the key will be a node at the tail and the values
    # will be the nodes at the heads of the directed section
    # So, (a, b) = a --> b and the key would be a with a value of b. 
    node_edges = defaultdict(list)

    with open("SCC.txt") as f:
        # Exclude the newline character, \n
        line_number = 1
        for line in f:
            # Remove the trailing space and newline characters.
            # Otherwise, there are issues on import
            line = line.rstrip(' \n')
            line = line.split(' ')

            source_node = int(line[0])
            # Due to use of defaultdict add sink nodes. The reason is
            # that with defaultdict when a key that is not in the 
            # dictionary is searched the defaultdict will add an entry
            # changing the size of the dictionary which is bad joojoo 
            # when iterating over a dictionary and will result in:
            # RuntimeError: dictionary changed size during iteration.
            while line_number < source_node:
                node_edges[line_number].append(line_number)
                line_number += 1
            
            node_edges[source_node].append(int(line[1]))
            line_number = source_node + 1

    return node_edges

def topological_sort(node_edges):
    """
    Outer loop for depth-first search to keep track of a vertex's order
    of precedence.
    """
    
    # Mark all nodes as unexplored
    is_explored = defaultdict(bool)
    for key in node_edges.keys():
        is_explored[key] = False
    
    # Keeps track of topological order
    # precedence_order, a larger number means it has lower precedence
    precedence_order = len(node_edges)
    topological_order = defaultdict(int)

    for u in node_edges.keys():
        if is_explored[u] == False:
            precedence_order = depth_first_search(node_edges, u, is_explored, 
                                precedence_order, topological_order)

    return topological_order

def depth_first_search(node_edges, u, is_explored, precedence_order, 
                        topological_order):
    """
    Depth first search implementation. Searches a directed graph until
    the search hits an explored node and returns where the node is 
    in relation to the other vertices.
    """

    is_explored[u] = True

    for v in node_edges[u]:
        if is_explored[v] == False:
            precedence_order = depth_first_search(node_edges, v, is_explored, 
                                precedence_order, topological_order)

    topological_order[u] = precedence_order
    precedence_order -= 1
    
    return precedence_order

def write_to_file(topological_order):
    """
    Writes the topological order to a file for inspection.
    """

    with open("topological_order.txt","w") as f:
        for k, v in sorted(topological_order.items()):
            f.write("{}\t\t\t{}\n".format(k, v))

    return os.getcwd()

if __name__ == "__main__":
    main()