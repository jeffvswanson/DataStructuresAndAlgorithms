# test_heap_sort.py

import heap_sort as hs
import unittest

class TestHS(unittest.TestCase):
    def test_parent(self):
        
        expected = [0, 1, 4]
        # Remember heapsort is a 1-based index
        # The 0 is a placeholder.
        # test_heap = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        children = [1, 3, 8]
        
        got = []
        for _, child_idx in children:
            got.append(hs.get_parent(child_idx))

        self.assertEqual(got, expected, 
        "Incorrect parent returned in get_parent.")


if __name__ == "__main__":
    unittest.main()