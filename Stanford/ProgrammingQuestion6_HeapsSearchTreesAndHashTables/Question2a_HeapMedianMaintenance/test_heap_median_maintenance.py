# test_heap_median_maintenance.py

import unittest

import heap as h
import heap_median_maintenance as hm

class TestHeapMedianMaintenance(unittest.TestCase):
    
    def test_rebalance(self):
        
        # Test 0, 0 element heap
        min_heap = h.Heap()
        max_heap = h.Heap("max")

        hm.rebalance(min_heap, max_heap)
        self.assertEqual(min_heap.length(), max_heap.length(), 
            "rebalance error, 0 element heaps should be equal")

        # Test 1, 0 element heap
        min_heap.insert(1)
        expected_min_length = min_heap.length()
        expected_max_length = max_heap.length()
        hm.rebalance(min_heap, max_heap)
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 1 element")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 0 elements")

        # Test 2, 0 element heap
        min_heap.insert(2)
        hm.rebalance(min_heap, max_heap)
        expected_min_length = 1
        expected_max_length = 1
        expected_max_root = 1
        got, prs = max_heap.peek()
        self.assertTrue(prs, "rebalance error, max_heap has no elements after rebalancing, should have 1 element")
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 1 element")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 1 element")
        self.assertEqual(got, expected_max_root, 
            "rebalance error, max-heap root incorrect")

        # Test 3, 0 element heap
        min_heap = h.Heap("min", 1, 2, 3)
        max_heap = h.Heap("max")
        hm.rebalance(min_heap, max_heap)
        expected_min_length = 2
        expected_max_length = 1
        expected_max_root = 1
        got, prs = max_heap.peek()
        self.assertTrue(prs, "rebalance error, max_heap has no elements after rebalancing, should have 1 element")
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 2 elements")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 1 element")
        self.assertEqual(got, expected_max_root, 
            "rebalance error, max_heap root incorrect")

        # Test 0, 1 element heap
        min_heap = h.Heap()
        max_heap = h.Heap("max", 1)
        expected_min_length = min_heap.length()
        expected_max_length = max_heap.length()
        hm.rebalance(min_heap, max_heap)
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 0 elements")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 1 element")

        # Test 0, 2 element heap
        max_heap.insert(2)
        expected_min_length = 1
        expected_max_length = 1
        expected_min_root = 2
        hm.rebalance(min_heap, max_heap)
        got, prs = min_heap.peek()
        self.assertTrue(prs, "rebalance error, min_heap has no elements after rebalancing, should have 1 element")
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 1 element")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 1 element")
        self.assertEqual(got, expected_min_root, 
            "rebalance error, min_heap root incorrect")

        # Test 0, 3 element heap
        min_heap = h.Heap()
        max_heap = h.Heap("max", 1, 2, 3)
        expected_min_length = 1
        expected_max_length = 2
        expected_min_root = 3
        hm.rebalance(min_heap, max_heap)
        got, prs = min_heap.peek()
        self.assertTrue(prs, "rebalance error, min_heap has no elements after rebalancing, should have 1 element")
        self.assertEqual(min_heap.length(), expected_min_length, 
            "rebalance error, min_heap should have 1 element")
        self.assertEqual(max_heap.length(), expected_max_length, 
            "rebalance error, max_heap should have 1 element")
        self.assertEqual(got, expected_min_root, 
            "rebalance error, min_heap root incorrect")

    def test_find_median(self):
        
        # Test an even number of elements when heap lengths combined
        min_heap = h.Heap("min", 10, 9, 8, 7)
        max_heap = h.Heap("max", 0, 1, 2, 3)
        expected = 3
        got = hm.find_median(min_heap, max_heap)
        self.assertEqual(got, expected)

        # Test an odd number of elements when heap lengths combined
        # and median index greater than the number of elements in 
        # heap containing low elements
        min_heap.insert(11)
        expected = 7
        got = hm.find_median(min_heap, max_heap)
        self.assertEqual(got, expected)

        # Test an odd number of elements when heap lengths combined
        # And median index the same or less than the heap containing 
        # low elements
        max_heap.insert(4)
        max_heap.insert(5)
        expected = 5
        got = hm.find_median(min_heap, max_heap)
        self.assertEqual(got, expected)

    def test_find_last_four(self):
        
        test_total = 89178765
        expected = 8765
        got = hm.find_last_four(test_total)
        self.assertEqual(expected, got, "find_last_four() failure.")

if __name__ == "__main__":
    unittest.main()