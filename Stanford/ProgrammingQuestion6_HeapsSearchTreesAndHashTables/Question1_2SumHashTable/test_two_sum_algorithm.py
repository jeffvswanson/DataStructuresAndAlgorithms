# test_two_sum_algorithm.py

import unittest
import two_sum_algorithm as tsa

class TestPQ6_Part1(unittest.TestCase):
    def test_setup(self):
        # expected length of the target values set
        expected_length = 20001

        # first and last values in algo1-programming-2sum.txt
        values = [68037543430, -60012933873]
        
        got = tsa.setup()

        self.assertEqual(expected_length, len(got[1]), "setup error expected length incorrect")

        for v in values:
            self.assertIn(v, got[0], "not all values loaded into set")

    def test_two_sum_search(self):

        values = {15, -15, 30, -99, 0}
        targets = set()
        for x in range(-15, 16):
            targets.add(x)

        expected = 3
        got = tsa.two_sum_search(values, targets)
        
        self.assertEqual(got, expected, "two_sum_search returns incorrect number of target values")

if __name__ == "__main__":
    unittest.main()