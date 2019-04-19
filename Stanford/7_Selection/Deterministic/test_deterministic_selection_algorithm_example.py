import deterministic_selection_algorithm_example as ds
import unittest

class TestDeterministicSelectionAlgorithm(unittest.TestCase):
    def test_find_median_of_medians(self):
        """
        Test that the function returns the index of the median of
        medians of a given list.
        """

        data = [0, 4, 5, 1, 9]
        result = ds.find_median_of_medians(data)

        self.assertEqual(result, 2)

    def test_selection_sort(self):
        """
        Test selection sort returns the bounded section of the 
        list, sorted.
        """

        data = [0, 4, 5, 1, 9, 2, 7, 3, 6, 8]
        
        left_index = 5
        right_index = len(data)-1

        result = ds.selection_sort(data, left_index, right_index)
        expected_list = [0, 4, 5, 1, 9, 2, 3, 6, 7, 8]

        self.assertEqual(result, expected_list)

    def test_swap(self):
        """
        Test that the swap function swaps values in a list.
        """

        data = [1, 2]
        result = ds.swap(data, 0, 1)
        expected = [2, 1]

        self.assertEqual(result, expected)

    def test_find_last_digit(self):
        """
        Test that the find_last_digit function correctly returns the
        last digit of a decimal number.
        """

        data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []

        for val in data:
            result.append(ds.find_last_digit(val))

        self.assertEqual(result, expected)
        
    def test_output_first(self):
        """
        Test that the 'first' output message gets selected.
        """
        data = [1, 11, 4]
        correct_output = "The 1st order statistic is 6."
        
        result = []
        expected = [True, False, False]

        for val in data:
            actual_output = ds.output(val, 6, ds.find_last_digit(val))
            if actual_output == correct_output:
                result.append(True)
            else:
                result.append(False)

        self.assertEqual(result, expected)

    def test_output_second(self):
        """
        Test that the 'second' output message gets selected.
        """
        data = [2, 12, 4]
        correct_output = "The 2nd order statistic is 6."
        
        result = []
        expected = [True, False, False]

        for val in data:
            actual_output = ds.output(val, 6, ds.find_last_digit(val))
            if actual_output == correct_output:
                result.append(True)
            else:
                result.append(False)

        self.assertEqual(result, expected)

    def test_output_third(self):
        """
        Test that the 'third' output message gets selected.
        """
        data = [3, 13, 4]
        correct_output = "The 3rd order statistic is 6."
        
        result = []
        expected = [True, False, False]

        for val in data:
            actual_output = ds.output(val, 6, ds.find_last_digit(val))
            if actual_output == correct_output:
                result.append(True)
            else:
                result.append(False)

        self.assertEqual(result, expected)

    def test_output_otherwise(self):
        """
        Test that the '-th' output message gets selected.
        """
        data = [1, 2, 3, 14]
        correct_output = "The 14th order statistic is 6."
        
        result = []
        expected = [False, False, False, True]

        for val in data:
            actual_output = ds.output(val, 6, ds.find_last_digit(val))
            if actual_output == correct_output:
                result.append(True)
            else:
                result.append(False)

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()