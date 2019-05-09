# test_breadth_first_search.py

import breadth_first_search as bfs
import unittest

from collections import defaultdict

class TestBFS(unittest.TestCase):
    def test_setup(self):
        """
        Test to ensure lists are set up correctly for the problem.
        """

        result = bfs.setup()

        vertices = result[0]
        node_edges = result[1]

        # 200 is the last vertex value
        self.assertEqual(vertices[-1], 200, 
        "The vertices list has not imported correctly.")

        # Check that the one-to-many relationship of a vertex to other
        # vertices is hashed correctly. Using node 200.
        expected = [149, 155, 52, 87, 120, 39, 160, 137, 27, 79, 131, 100, 25, 
        55, 23, 126, 84, 166, 150, 62, 67, 1, 69, 35]
        self.assertEqual(node_edges[200], expected)  

    def test_breadth_first_search(self):
        """
        Tests the three possible outcomes of a breadth first search:
        1) A path exists between two seperate nodes.
        2) A node is a path unto itself, distance = 0.
        3) No path exists between two nodes, distance = -1.
        """

        expected = [2, 0, -1]
        test_type = ["a path exists.", 
        "the starting node is the same as the ending node.", "no path exists."]
        vertices = [1, 2, 3, 4]
        starting_node = 1
        ending_node = [4, 1, 3]

        node_edges = defaultdict(list)
        node_edges_list = [(1, 2), (2, 1), (2, 4), (4, 2)] 
        for k, v in node_edges_list:
            node_edges[k].append(v)

        got = []
        for i in range(len(expected)):
            got.append(bfs.breadth_first_search(starting_node, ending_node[i], 
            vertices, node_edges))

        for i in range(len(expected)):
            self.assertEqual(expected, got, 
            "breadth_first_search does not return the correct shortest path when {}".format(test_type[i]))

    def test_output(self):
        """
        Test to ensure all output cases are covered.
        """

        shortest_path = [-1, 0, 1]
        starting_node = [ 1, 1, 1]
        ending_node = [19, 1, 2]
        test_type = ["Not Connected", 
        "Ending Node is the same as the Starting Node", "Shortest Path"]

        expected = []
        # Not connected result.
        expected.append("Nodes {} and {} are not connected.".format(starting_node[0], 
        ending_node[0]))
        # Starting node is the same as the ending node.
        expected.append("The shortest path is 0. If you're at home, you don't have to cross the street to get home!")
        # A shortest path exists
        expected.append("The shortest path between nodes {} and {} is {}.".format(starting_node[2], 
        ending_node[2], shortest_path[2]))

        result = []
        for i in range(len(test_type)):    
            result.append(bfs.generate_output(shortest_path[i], 
            starting_node[i], ending_node[i]))
        
        for i in range(len(expected)):
            self.assertEqual(expected[i], result[i], 
            "The output message is not correct on the {} test".format(test_type[i]))

if __name__ == "__main__":
    unittest.main()