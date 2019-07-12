# test_heap_median_maintenance.py

import unittest

import heap_median_maintenance as hm

class TestHeapMedianMaintenance(unittest.TestCase):
    
    def test_rebalance(self):
        pass

    def test_find_median(self):
        pass

    def test_find_last_four(self):
        
        test_total = 89178765
        expected = 8765
        got = hm.find_last_four(test_total)

        self.assertEqual(expected, got, "find_last_four() failure.")

if __name__ == "__main__":
    unittest.main()