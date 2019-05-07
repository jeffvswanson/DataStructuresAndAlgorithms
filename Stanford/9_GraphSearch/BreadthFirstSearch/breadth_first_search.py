# breadth_first_search.py
"""A demonstration program of the breadth first search (BFS) of an 
undirected graph to demonstrate BFS's shortest path capabilities."""

from collections import defaultdict

def main():
    print("This program demonstrates the shortest path characteristic \
of breadth first search (BFS) on an undirected graph.\n")

    vertices, node_edges = setup()

    starting_node = get_node_value("start")
    ending_node = get_node_value("end")

    shortest_path = breadth_first_search(starting_node, ending_node, 
    vertices, node_edges)

    output = generate_output(shortest_path, starting_node, ending_node)
    print(output)

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
            # Otherwise, there are issues on import.
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

def get_node_value(type_of_node):
    """
    Gets user input to designate a starting or ending node.
    """

    while True:
        if type_of_node == "start":
            try:
                node = int(input("Please enter your starting node choice \
(whole number between 1 and 200: "))
                if node < 1 or node > 200: raise ValueError
                break
            except (TypeError, ValueError, SyntaxError):
                print("That is not a whole number between 1 and 200, please try again\n")
        else:
            try:
                node = int(input("\nPlease enter your ending node choice \
(whole number between 1 and 200: "))
                if node < 1 or node > 200: raise ValueError
                break
            except (TypeError, ValueError, SyntaxError):
                print("That is not a whole number between 1 and 200, please try again\n")

    return node

def breadth_first_search(starting_node, ending_node, vertices, node_edges):
    """
    Function to explore the given graph for a connection between the 
    starting node and the ending node and return the shortest path 
    between the two nodes if one exists.
    """

    # Short circuit if the starting_node equals the ending_node
    if starting_node == ending_node:
        return 0

    # Set all nodes as unexplored
    isExplored = defaultdict(str)
    for vertex in vertices:
        isExplored[vertex] = "Unexplored"

    # Set starting_node as "Explored"
    isExplored[starting_node] = "Explored"

    # Let Q = queue data structure (First-in, First-out (FIFO)), 
    # initialized with starting_node
    q = [starting_node]

    # dist is a key-value pair representing how many edges we've 
    # traversed from the starting_node
    distance_from_start_node = defaultdict(int)
    distance_from_start_node[starting_node] = 0

    while len(q) != 0:
        v = q.pop(0)
        # Explore the different edges v posseses (v, u)
        for u in node_edges[v]:
            if isExplored[u] == "Unexplored":
                distance_from_start_node[u] = distance_from_start_node[v] + 1
                isExplored[u] = "Explored"
                q.append(u)

    if isExplored[ending_node] == "Explored":
        shortest_path = distance_from_start_node[ending_node]
    else:
        # The two nodes are not connected.
        shortest_path = -1

    return shortest_path

def generate_output(shortest_path, starting_node, ending_node):
    """
    Generates the message to the user detailing the result of the 
    breadth first search to find the shortest path.
    """

    if shortest_path < 0:
        output_message = "Nodes {} and {} are not connected.".format(starting_node, ending_node)
    elif shortest_path == 0:
        output_message = "The shortest path is 0. If you're at home, you don't have to \
cross the street to get home!"
    else:
        output_message = "The shortest path between nodes {} and {} is {}.".format(starting_node, ending_node, shortest_path)

    return output_message

if __name__ == "__main__":
    main()