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
        node_edges = result[1]

        # 200 is the last vertex value
        self.assertEqual(vertices[-1], 200, 
        "The vertices list has not imported correctly.")

        # Check that the one-to-many relationship of a vertex to other
        # vertices is hashed correctly. Using node 200.
        expected = [149, 155, 52, 87, 120, 39, 160, 137, 27, 79, 131, 100, 25, 
        55, 23, 126, 84, 166, 150, 62, 67, 1, 69, 35]
        self.assertEqual(node_edges[200], expected)


    def test_find_min_cuts(self):
        """
        Test to ensure min cut returns correct value.
        """
        
        vertices = [1, 2, 3, 4]
        node_edges = defaultdict(list)
        node_edges = {
            1: [2, 3], 
            2: [1, 3, 4], 
            3: [1, 2, 4], 
            4: [2, 3]
            }

        expected = 2
        got = pq.find_min_cuts(vertices, node_edges)

        self.assertEqual(expected, got, 
        "Min cut is not correct on length {} test".format(len(vertices)))

        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        node_edges = {
            1: [2, 3, 4, 5],
            2: [1, 3, 4, 5],
            3: [1, 2, 4, 5, 6],
            4: [1, 2, 3, 5, 7],
            5: [1, 2, 3, 4],
            6: [7, 8, 9, 10, 3],
            7: [6, 8, 9, 10, 4],
            8: [6, 7, 9, 10],
            9: [6, 7, 8, 10],
            10: [6, 7, 8, 9]
        }

        expected = 2
        got = pq.find_min_cuts(vertices, node_edges)

        self.assertEqual(expected, got, 
        "Min cut is not correct on length {} test".format(len(vertices)))

        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        node_edges = {
            1: [2, 3, 4, 5],
            2: [1, 3, 4, 5],
            3: [1, 2, 4, 5, 6],
            4: [1, 2, 3, 5, 7, 14],
            5: [1, 2, 3, 4],
            6: [7, 8, 9, 10, 3],
            7: [6, 8, 9, 10, 4],
            8: [6, 7, 9, 10],
            9: [6, 7, 8, 10],
            10: [6, 7, 8, 9],
            11: [12, 13, 14, 15],
            12: [11, 13, 14, 15],
            13: [12, 11, 14, 15],
            14: [12, 13, 11, 15, 4],
            15: [12, 13, 14, 11]
        }

        expected = 1
        got = pq.find_min_cuts(vertices, node_edges)

        self.assertEqual(expected, got, 
        "Min cut is not correct on length {} test".format(len(vertices)))

if __name__ == "__main__":
    unittest.main()