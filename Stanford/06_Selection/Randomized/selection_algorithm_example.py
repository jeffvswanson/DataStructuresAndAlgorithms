# selection_algorithm_example.py
"""
An example of a linear runtime selection algorithm leveraging quicksort
principles.
"""

from random import randint

def main():
    target_list = [9, 8, 2, 1, 5, 7, 0, 4, 6, 3]
    
    k_order_statistic = randint(1, len(target_list))
    
    _, target_value = quick_selection(target_list, k_order_statistic)

    last_digit = k_order_statistic%10

    if last_digit == 1:
        print("The {}st order statistic is {}.".format(k_order_statistic, 
        target_value))
    elif last_digit == 2:
        print("The {}nd order statistic is {}.".format(k_order_statistic, 
        target_value))
    elif last_digit == 3:
        print("The {}rd order statistic is {}.".format(k_order_statistic, 
        target_value))
    else:
        print("The {}th order statistic is {}.".format(k_order_statistic, 
        target_value))

def quick_selection(target_list, k):
    # Base case: if the list length is less than 1 the list is sorted.
    if len(target_list) < 2:
        return target_list, target_list[0]

    pivot_index = randint(0, len(target_list)-1)
    pivot_value = target_list[pivot_index]

    # Swap the pivot index with the leftmost element.
    target_list = swap(target_list, pivot_index, 0)

    # Set pointers for partitions.
    # i is the pointer for the index where all elements in positions
    # less than index i are less than or equal to the pivot.
    # j is the pointer to the index where all elements in positions
    # greater than the index j have not yet been compared to the pivot.
    i = j = 1
     
    while j < len(target_list):
        if target_list[j] < pivot_value:
            target_list = swap(target_list, i, j)
            i += 1
        j += 1

    # Set the index of where the pivot should reside.
    pivot_index = i - 1

    # Place the pivot in its rightful place.
    target_list = swap(target_list, 0, pivot_index)

    # Determine how to continue solving the problem.
    # Remember, k is on a 1-based index and pivot_index is 0-based.
    if k-1 == pivot_index:
        return target_list, target_list[pivot_index]
    elif k-1 < pivot_index:
        return quick_selection(target_list[:pivot_index], k)
    else:
        return quick_selection(target_list[i:], k-i)

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

if __name__ == "__main__":
    main()