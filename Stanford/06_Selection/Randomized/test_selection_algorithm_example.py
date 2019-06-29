import selection_algorithm_example as sa
import unittest

class TestSelectionAlgorithm(unittest.TestCase):
    def test_swap(self):
        """
        Test that swap function will swap values in a list.
        """

        data = [1, 2]
        result = sa.swap(data, 0, 1)
        self.assertEqual(result, [2, 1])

    def test_quick_selection(self):
        """
        Test quick selection returns the k-th order statistic in a 
        list of numbers.
        """

        data = [8, 7, 9, 0, 1, 3, 6, 5, 2, 4]
        k = 2

        _, result = sa.quick_selection(data, k)

        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
