# test_depth_first_search.py

import unittest
import depth_first_search as dfs

class TestDFS(unittest.TestCase):
    def test_setup(self):
        """
        Test to ensure relationships between nodes and edges are set up
        correctly for the problem.
        """

        result = dfs.setup()

        max_node = list(result.keys())[-1]

        # 875714 is the last vertex value
        self.assertEqual(max_node, 875714, 
        "The vertices have not imported correctly. \
Expected: 875714, Got: {}".format(max_node))

        # Check that the one-to-many relationship of a vertex to other 
        # vertices is hashed correctly. Using node 875714.
        expected = [542446, 13655, 542447, 13656, 542448, 542449, 542450, 
                    542451, 542452, 13660, 9434, 542453]
        self.assertEqual(result[max_node], expected, 
        "The edges have not imported correctly.\n\
Expected:\t{}\n\
Got:\t\t{}".format(expected, result[max_node]))

if __name__ == "__main__":
    unittest.main()