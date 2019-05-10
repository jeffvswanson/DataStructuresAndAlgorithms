# depth_first_search.py
"""Demonstration program of the depth first search (DFS) of a directed
graph to demonstrate DFS's topological sort capabilities."""

from collections import defaultdict

def main():

    print("This program demonstrates the topological sort characteristic \
of depth first search (DFS) on a directed graph.\n", flush=True)

    node_edges = setup()

    precedence_order = topological_sort(node_edges)
    
    print("is_explored[50] = {}".format(precedence_order[50]), flush=True)
    print("is_explored[145678] = {}".format(precedence_order[145678]), flush=True)
    #print("The precedent order of 50 is {}".format(precedence_order[50]))

def setup():
    """
    Converts the SCC.txt file into a python useable format.
    """

    # For node_edges the key will be a node at the tail and the values
    # will be the nodes at the heads of the directed section
    # So, (a, b) = a --> b and the key would be a with a value of b. 
    node_edges = defaultdict(list)

    with open("SCC.txt") as f:
        # Exclude the newine character, \n
        for line in f:
            # Remove the trailing space and newline characters.
            # Otherwise, there are issues on import
            line = line.rstrip(' \n')
            line = line.split(' ')

            node_edges[int(line[0])].append(int(line[1]))

    return node_edges

def topological_sort(node_edges):
    
    # Mark all nodes as unexplored
    is_explored = defaultdict(bool)
    for key in node_edges.keys():
        is_explored[key] = False
    
    # Keeps track of topological order
    # current_precedence = len(node_edges)
    # topological_order = defaultdict(int)
    
    for u in node_edges.keys():
        if is_explored[u] == False:
            is_explored = depth_first_search(node_edges, u, is_explored)
            
            #topological_order[u], is_explored[u], current_precedence \
            #    = depth_first_search(node_edges, u, current_precedence, 
            #                        is_explored)

    return is_explored# topological_order

#def depth_first_search(node_edges, u, current_precedence, is_explored):
def depth_first_search(node_edges, u, is_explored):

    is_explored[u] = True

    for v in node_edges[u]:
        if is_explored[v] == False:
            is_explored = depth_first_search(node_edges, v, is_explored)
    #         current_precedence, is_explored[v], _ \
    #             = depth_first_search(node_edges, v, current_precedence, 
    #                                 is_explored)
    # topological_order = current_precedence
    # current_precedence -= 1
    # print("current_precedence =", current_precedence)
    
    return is_explored #topological_order, is_explored[u], current_precedence

if __name__ == "__main__":
    main()