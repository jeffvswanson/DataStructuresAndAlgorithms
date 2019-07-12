# test_heap.py

import unittest
import heap as h

class TestHeap(unittest.TestCase):

    def test_init(self):

        min_heap = h.Heap()
        expected_length = 1
        
        # Empty heap instantiated with a 0 at index position 0.
        self.assertEqual(expected_length, len(min_heap.heap), 
            "empty min-heap does not have correct length. Expected: {}, Got {}".format(expected_length, len(min_heap.heap)))

        min_heap = h.Heap("min", 1, 2)
        expected_length = 3
        self.assertEqual(expected_length, len(min_heap.heap),
            "instantiated min-heap does not have correct length. Expected {}, Got {}".format(expected_length, len(min_heap.heap)))

        max_heap = h.Heap("max")
        expected_length = 1
        self.assertEqual(expected_length, len(max_heap.heap),
            "empty max-heap does not have correct length. Expected: {}, Got {}".format(expected_length, len(max_heap.heap)))

    def test_insert_and_bubble_up(self):

        min_heap = h.Heap()
        max_heap = h.Heap("max")
        insert_elements = [3, 1, -4, 99, 0]
        expected_length = 1

        for element in insert_elements:
            min_heap.insert(element)
            max_heap.insert(element)
            expected_length += 1

        # Empty heap instantiated with a 0 at index position 0.
        expected_order = [0, -4, 0, 1, 99, 3]
        self.assertEqual(expected_order, min_heap.heap, "insert failed.")

        # Remember the max-heap implementation negates values on insert
        expected_order = [0, -99, -3, 4, -1, 0]
        self.assertEqual(expected_order, max_heap.heap, "insert failed.")

    def test_extract_root_and_bubble_down(self):

        min_heap = h.Heap()
        max_heap = h.Heap("max")
        insert_elements = [3, 1, -4, 99, 0]
        expected_length = 1

        for element in insert_elements:
            min_heap.insert(element)
            max_heap.insert(element)
            expected_length += 1

        expected_min_extraction = [-4, 0, 1, 3, 99]
        expected_max_extraction = [99, 3, 1, 0, -4]
        actual_min_extraction, actual_max_extraction = [], []

        for i in range(1, expected_length+1):
            root, present = min_heap.extract_root()
            if present:
                actual_min_extraction.append(root)

            root, present = max_heap.extract_root()
            if present:
                actual_max_extraction.append(root)

        self.assertEqual(expected_min_extraction, actual_min_extraction, "min-heap extract_root() failed")
        self.assertEqual(expected_max_extraction, actual_max_extraction, "max-heap extract_root() failed")

        # Attempt to extract a root from an empty heap
        _, present = min_heap.extract_root()
        self.assertFalse(present, "min-heap extract_root() failed trying to extract a root that does not exist")

        _, present = max_heap.extract_root()
        self.assertFalse(present, "max-heap extract_root() failed trying to extract a root that does not exist")

    def test_get_parent_index(self):

        # Remember, heaps are a 1-based index
        min_heap = h.Heap("min", 1, 2, 3, 4, 5)
        test_indices = [1, 2, 4]
        expected = [False, 1, 2]
        got = []
        
        for i in test_indices:
            got.append(min_heap.get_parent_index(i))
        
        self.assertEqual(expected, got, "get_parent_index failed")

    def test_left_child_index(self):

        # Remember, heaps are a 1-based index
        max_heap = h.Heap("max", 1, 2, 3, 4, 5)
        test_indices = [1, 2, 4]
        expected = [2, 4, False]
        got = []

        for i in test_indices:
            got.append(max_heap.get_left_child_index(i))
        
        self.assertEqual(expected, got, "get_left_child_index failed")

    def test_right_child_index(self):
        
        # Remember, heaps are a 1-based index
        min_heap = h.Heap("min", 1, 2, 3, 4, 5)
        test_indices = [1, 2, 4]
        expected = [3, 5, False]
        got = []

        for i in test_indices:
            got.append(min_heap.get_right_child_index(i))
        
        self.assertEqual(expected, got, "get_right_child_index failed")

    def test_peek(self):
        
        min_heap = h.Heap()
        max_heap = h.Heap("max")

        # Attempt to check a heap with no root
        _, present = min_heap.peek()
        self.assertFalse(present, "min_heap.peek() failed. There should be no root on an empty heap.")

        _, present = max_heap.peek()
        self.assertFalse(present, "max_heap.peek() failed. There should be no root on an empty heap.")

        nodes = [1, 2, 3]

        for node in nodes:
            min_heap.insert(node)
            max_heap.insert(node)

        expected = (1, True)
        got = min_heap.peek()
        self.assertTupleEqual(expected, got, "min_heap.peek() failed. Root value is not correct.")

        expected = (3, True)
        got = max_heap.peek()
        self.assertTupleEqual(expected, got, "max_heap.peek() failed. Root value is not correct.")

    def test_length(self):
        
        min_heap = h.Heap()

        # Check the length of a heap with no elements added.
        expected = 0
        got = min_heap.length()
        self.assertEqual(expected, got, "heap.length() failed, incorrect heap length.")

        min_heap.insert(5)
        expected = 1
        got = min_heap.length()
        self.assertEqual(expected, got, "heap.length() failed, incorrect heap length.")

if __name__ == "__main__":
    unittest.main()