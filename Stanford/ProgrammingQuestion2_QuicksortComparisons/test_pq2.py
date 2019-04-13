import pq2_counting_comparisons_in_quicksort as pq
import unittest

class TestPQ2(unittest.TestCase):
    def test_select_pivot(self):
        """
        Test that select_pivot will select the correct method to choose
        a pivot index.
        """

        index_choices_list = ["first", "last", "median"]
        test_list = [2, 8, 4, 0]

        result = [] 

        for choice in index_choices_list:
            result.append(pq.select_pivot(test_list, 0, len(test_list)-1, choice))

        # Expected value is index positions
        self.assertEqual(result, [0, 3, 0])

    def test_selection_sort(self):
        """
        Test the implementation of selection sort.
        """

        unsorted_list = [2, 3, 1, 4]
        result = pq.selection_sort(unsorted_list)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_setup(self):
        """
        Test the setup function.
        """

        result = []
        result = pq.setup()

        self.assertEqual(result[-1], 9269)

    def test_swap(self):
        """
        Test that swap will swap values in a list.
        """

        data = [1, 2]
        result = pq.swap(data, 0, 1)
        self.assertEqual(result, [2, 1])

    def test_quicksort_sort_list(self):
        """
        Test that the quicksort function returns a sorted list.
        """

        test_list = [9, 4, 6, 1, 3, 7, 5, 2, 8, 0]

        sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result_list, _ = pq.quicksort(test_list, 0, len(test_list)-1, 0)
        self.assertEqual(result_list, sorted_list)

    def test_quicksort_comparisons_first(self):
        """
        Ensure quicksort returns the correct number of comparisons when
        the pivot selection method only selects the first element as
        the pivot.
        """

        test_list = [3, 1, 2]

        _, result = pq.quicksort(test_list, 0, len(test_list)-1, 0,
        pivot_method="first")

        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()