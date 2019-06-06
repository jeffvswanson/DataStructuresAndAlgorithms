# test_heap_sort.py

import copy
import heap_sort as hs
import unittest

class TestHeapSort(unittest.TestCase):
    def test_get_parent_index(self):
        """
        Test to ensure proper parent index is returned.
        """

        # Remember the 0 is a place-holder and heap has a 1-based index.
        # heap = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        expected = [0, 1, 4]
        find_parent = [1, 3, 8]

        got = []
        for child in find_parent:
            got.append(hs.get_parent_index(child))

        self.assertEqual(got, expected, 
        "get_parent_index did not return the correct indices.\
            \n\tExpected: {}, Got: {}".format(expected, got))

    def test_get_left_child_index(self):
        """
        Test to ensure proper left_child_index is returned.
        """

        # Remember, 0 is a place-holder and heap has a 1-based index.
        heap = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        expected_indices = [2, 6, 8, 0]
        parent_indices = [1, 3, 4, len(heap)-1]

        got = []
        for index in parent_indices:
            got.append(hs.get_left_child_index(index, heap))

        self.assertEqual(got, expected_indices,
        "get_left_child_index did not return the correct indices.\
            \n\tExpected: {}, Got: {}".format(expected_indices, got))

    def test_get_right_child_index(self):
        """
        Test to ensure proper right_child_index is returned.
        """

        # Remember, 0 is a place-holder and heap has a 1-based index.
        heap = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        expected_indices = [3, 7, 0, 0]
        parent_indices = [1, 3, 4, 8]

        got = []
        for index in parent_indices:
            got.append(hs.get_right_child_index(index, heap))

        self.assertEqual(got, expected_indices, 
        "get_right_child_index did not return the correct indices.\
            \n\tExpected: {}, Got: {}".format(expected_indices, got))

    def test_bubble_up(self):
        """
        Test to ensure bubble_up functions appropriately.
        """

        # Remember, 0 is a place-holder and heap has a 1-based index.
        original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected = [0, 1, 1, 3, 2, 5, 6, 7, 8, 4]

        heap = copy.deepcopy(original_list)
        # Check against the root node, nothing should change.
        hs.bubble_up(1, heap)
        self.assertEqual(heap, original_list,
        "bubble_up() failed. The root node should not bubble-up past index 1.\
            \n\tExpected: {}, Got: {}".format(original_list, heap))

        # Check against the value violating the heap property.
        heap.append(1)
        hs.bubble_up(len(heap)-1, heap)
        self.assertEqual(heap, expected,
        "bubble_up() failed.\
            \n\tExpected:\t{}\
            \n\tGot:\t\t{}".format(expected, heap))

    def test_insert(self):
        """
        Test to ensure inserting a key maintains the heap property.
        """

        # Remember, 0 is a place-holder and heap has a 1-based index.
        heap = [0]
        expected = [0, 1]

        hs.insert(1, heap)
        self.assertEqual(heap, expected, 
        "insert() failed. Expected: {}, Got {}".format(expected, heap))

        add = [4, 4, 8, 13, 5, 9, 3]
        expected = [0, 1, 3, 4, 4, 13, 5, 9, 8]
        for node in add:
            hs.insert(node, heap)

        self.assertEqual(heap, expected,
        "insert() failed.\
            \n\tExpected:\t{}\
            \n\tGot:\t\t{}".format(expected, heap))

    def test_heapify(self):
        """
        Test to ensure validity of heapify function.
        """

        unheaped = [11, 13, 9, 4, 12, 9, 4, 8, 4]
        # Remember, 0 is a place-holder and heap has a 1-based index.
        expected = [0, 4, 4, 4, 8, 12, 11, 9, 13, 9]

        got = hs.heapify(unheaped)

        self.assertEqual(got, expected,
        "heapify() failed.\
            \n\tExpected:\t{}\
            \n\tGot:\t\t{}".format(expected, got))

    def test_bubble_down(self):
        """
        Test to ensure proper function of bubble_down().
        """

        # Remember, 0 is a place-holder and heap is a 1-based index.
        heap = [0, 8, 2, 3, 4, 5, 6, 7]
        expected = [0, 2, 4, 3, 8, 5, 6, 7]

        hs.bubble_down(1, heap)

        self.assertEqual(heap, expected, 
        "bubble_down() failed.\
            \n\tExpected:\t{}\
            \n\tGot:\t\t{}".format(expected, heap))

    def test_extract_min(self):
        """
        Check on extract_min results.
        """

        # Remember, 0 is a place-holder and heap is a 1-based index.
        heap = [0]
        expected = 0
        got, heap = hs.extract_min(heap)
        self.assertEqual(got, expected, 
        "extract_min() failed. Expected: {}, Got: {}".format(expected, got))
        
        heap = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        got = []
        while len(heap) > 1:
            min_value, heap = hs.extract_min(heap)
            got.append(min_value)

        self.assertEqual(got, expected,
        "extract_min() failed.\
            \n\tExpected:\t{}\
            \n\tGot:\t\t{}".format(expected, got))

if __name__ == "__main__":
    unittest.main()