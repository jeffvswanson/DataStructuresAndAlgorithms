# test_pq3.py

import numpy as np
import pq3_find_min_cut as pq
import unittest
from collections import defaultdict

class TestPQ3(unittest.TestCase):
    def test_setup(self):
        """
        Test to ensure lists are set up correctly for the problem.
        """

        result = pq.setup()

        vertices = result[0]
        edges = result[1]
        edge_endpoints = result[2]
        node_edges = result[3]

        # 200 is the last vertex value
        self.assertEqual(vertices[-1], 200, 
        "The vertices list has not imported correctly.")

        # (200, 35) is the last edge value
        self.assertEqual(edges[-1], (200, 35), 
        "The edges list has not imported correctly.")

        # Check that there are no self-loops
        for i in vertices:
            self.assertNotIn(edges, (i, i), 
        "The edges list has self-loops. Remove the self-loops.")

        # Check that the one-to-many relationship of a vertex to other
        # vertices is hashed correctly. Using node 200.
        expected = [149, 155, 52, 87, 120, 39, 160, 137, 27, 79, 131, 100, 25, 
        55, 23, 126, 84, 166, 150, 62, 67, 1, 69, 35]
        self.assertEqual(node_edges[200], expected)


    def test_min_cut(self):
        """
        Test to ensure min cut returns correct value.
        """
        
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (1, 3), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), 
        (3, 4), (4, 2), (4, 3)]
        node_edges = defaultdict(list)
        node_edges = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

        expected = 2
        got = pq.find_min_cut(vertices, edges, node_edges)

        self.assertEqual(expected, got, "Min cut is not correct.")

if __name__ == "__main__":
    unittest.main()