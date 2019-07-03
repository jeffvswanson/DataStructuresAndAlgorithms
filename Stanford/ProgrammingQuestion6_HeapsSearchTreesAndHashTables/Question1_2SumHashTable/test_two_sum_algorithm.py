# test_two_sum_algorithm.py

import unittest
import two_sum_algorithm as tsa

class TestPQ6_Part1(unittest.TestCase):
    def test_setup(self):
        # expected length of target values set
        expected_length = 20001
        # first and last values in algo1-programming-2sum.txt
        values = [68037543430, -60012933873]
        
        got = tsa.setup()

        self.assertEqual(expected_length, len(got[1]), "setup error expected length incorrect")

        for v in values:
            self.assertIn(v, got[0], "not all values loaded into set")

if __name__ == "__main__":
    unittest.main()