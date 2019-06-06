# deterministic_selection_algorithm_example.py
"""
An example of using the deterministic "median of medians" method to 
conduct a selection in linear, O(n), runtime.
"""

from random import randint

def main():
    target_list = [7, 2, 17, 12, 13, 8, 20, 4, 6, 3, 19, 1, 9, 5, 16, 10, 15, 
    18, 14, 11]

    k_order_statistic = randint(1, len(target_list))

    _, target_value = quick_select(target_list, k_order_statistic)

    last_digit = find_last_digit(k_order_statistic)

    print("From the list")
    print(sorted(target_list))
    result = output(k_order_statistic, target_value, last_digit)
    print(result)

def quick_select(target_list, k):
    # Base case: A list of length 1 or 0 is by default sorted.
    if len(target_list) < 2:
        return target_list, target_list[0]

    pivot_index = find_median_of_medians(target_list)
    pivot_value = target_list[pivot_index]

    # Swap the pivot value to the leftmost index position
    target_list = swap(target_list, 0, pivot_index)

    # Set up the pointers
    # i is the index delineating the partition of all values less 
    # than or equal to the pivot.
    # j is the index value of which all indices greater than j have not
    # yet been compared against the pivot value.
    i = j = 1

    # Perform the sort
    while j < len(target_list):
        if target_list[j] <= pivot_value:
            target_list = swap(target_list, i, j)
            i += 1
        j += 1
    
    # Swap the pivot value into its rightful position
    pivot_index = i - 1
    target_list = swap(target_list, 0, pivot_index)

    # Determine how to continue solving the problem.
    # Remember, k is on a 1-based index and pivot_index is 0-based.
    if k-1 == pivot_index:
        return target_list, target_list[pivot_index]
    elif k-1 < pivot_index:
        return quick_select(target_list[:pivot_index], k)
    else:
        return quick_select(target_list[i:], k-i)


def find_median_of_medians(target_list):
    """Method to select the median of medians from a list."""

    group_size = 5

    # Base case: A list less than the group size is close enough.
    if len(target_list) < group_size:
        return len(target_list)//2

    num_full_groups = len(target_list)//group_size
    medians = []
    median_indices = []

    for i in range(0, num_full_groups*group_size, group_size):
        target_list = selection_sort(target_list, i, i+5)
        medians.append(target_list[i+2])
        median_indices.append(i+2)

    _, median_of_medians = quick_select(medians, 
    len(target_list)//(group_size*2))

    for idx, potential_median in enumerate(medians):
        if potential_median == median_of_medians:
            median_of_medians_index = median_indices[idx]

    return median_of_medians_index

def selection_sort(given_list, left_index, right_index):
    """Will always sort 5 elements. Used to determine median values."""

    for idx in range(left_index, right_index):
        min_value = given_list[idx]
        min_index = idx
        j = idx + 1
        while j < right_index:
            if given_list[j] < min_value:
                min_value = given_list[j]
                min_index = j
            j += 1
        given_list = swap(given_list, idx, min_index)
    
    return given_list

def swap(L, i, j):
    """Swaps values at indices i and j in list L."""

    L[i], L[j] = L[j], L[i]
    return L

def find_last_digit(k):
    """Determines the last digit in a base 10 integer."""

    return k%10

def output(k_order_statistic, target_value, last_digit):
    if k_order_statistic != 11 and last_digit == 1:
        result = "The {}st order statistic is {}.".format(k_order_statistic, 
        target_value)
    elif k_order_statistic != 12 and last_digit == 2:
        result = "The {}nd order statistic is {}.".format(k_order_statistic, 
        target_value)
    elif k_order_statistic != 13 and last_digit == 3:
        result = "The {}rd order statistic is {}.".format(k_order_statistic, 
        target_value)
    else:
        result = "The {}th order statistic is {}.".format(k_order_statistic, 
        target_value)
    return result

if __name__ == "__main__":
    main()