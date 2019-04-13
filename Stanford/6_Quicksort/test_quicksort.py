import quicksort as qs
import unittest


class TestSwap(unittest.TestCase):
    def test_swap(self):
        """
        Test that swap will swap values in a list.
        """
        data = [1, 2]
        result = qs.swap(data, 0, 1)
        self.assertEqual(result, [2, 1])

    def test_quicksort(self):
        """
        Test that quicksort returns a list in ascending order.
        """
        data = [20, 14, 6, 7, -10, 0, 58]
        result = qs.quicksort(data, 0, len(data)-1)
        self.assertEqual(result, [-10, 0, 6, 7, 14, 20, 58])

if __name__ == "__main__":
    unittest.main()