# pq2_counting_comparisons_in_quicksort.py
"""Programming question 2 from Stanford Datastructures and Algorithms

The file, quicksort.txt, contains all of the integers between 1 and 
10,000 inclusive, with no repeats) in unsorted order. The integer in 
the i-th row of the file gives you the i-th entry of an input array.

Your task is to compute the total number of comparisons used to sort 
the given input file by QuickSort. As you know, the number of 
comparisons depends on which elements are chosen as pivots, so we'll 
ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a 
recursive call on a subarray of length m, you should simply add m-1 to
your running total of comparisons. (This is because the pivot element 
is compared to each of the other m - 1 elements in the subarray in this
recursive call.)

WARNING: The Partition subroutine can be implemented in several 
different ways, and different implementations can give you differing 
numbers of comparisons. For this problem, you should implement the 
Partition subroutine exactly as it is described in the video lectures 
(otherwise you might get the wrong answer).

Question 1
For the first part of the programming assignment, you should always use
the first element of the array as the pivot element.

Question 2
Compute the number of comparisons (as in Problem 1), always using the 
final element of the given array as the pivot element. Again, be sure 
to implement the Partition subroutine exactly as it is described in 
the video lectures.

Question 3
Compute the number of comparisons (as in Problem 1), using the 
"median-of-three" pivot rule. [The primary motivation behind this rule
is to do a little bit of extra work to get much better performance on 
input arrays that are nearly sorted or reverse sorted.] In more 
detail, you should choose the pivot as follows. Consider the first, 
middle, and final elements of the given array. (If the array has odd 
length it should be clear what the "middle" element is; for an array 
with even length 2k, use the k-th element as the "middle" element. So 
for the array 4 5 6 7, the "middle" element is the second one ---- 5 
and not 6!) Identify which of these three elements is the median 
(i.e., the one whose value is in between the other two), and use this 
as your pivot. As discussed in the first and second parts of this 
programming assignment, be sure to implement Partition exactly as 
described in the video lectures (including exchanging the pivot 
element with the first element just before the main Partition 
subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first 
(8), middle (4), and last (1) elements; since 4 is the median of the 
set {1,4,8}, you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons 
made in identifying the median of the three candidate elements. You 
should NOT do this. That is, as in the previous two problems, you 
should simply add m - 1 to your running total of comparisons every 
time you recurse on a subarray with length m.
"""

import sys
from random import randint

def main():
    print("Setting up")
    initial_list = setup()

    # Copy the lists to prevent Python from referencing the memory 
    # locations
    question_list = initial_list.copy()

    # Set up list to aggregate number of comparisons used per pivot
    # selection method
    comparisons_list = [0, 0, 0]
    print("Calculating first item pivot method.")
    comparisons_list[0] = quicksort(question_list, 0, len(question_list)-1, 
    comparisons_list[0], pivot_method="first")
    print("Calculating last item pivot method.")
    question_list = initial_list.copy()
    comparisons_list[1] = quicksort(question_list, 0, len(question_list)-1, 
    comparisons_list[1], pivot_method="last")
    print("Calculating median of three pivot method.")
    question_list = initial_list.copy()
    comparisons_list[2] = quicksort(initial_list, 0, len(question_list)-1, 
    comparisons_list[2], pivot_method="median")
    print("Calculations complete.")

    print("There are {} comparisons using the first element as the pivot " 
        "element.".format(comparisons_list[0]))

    print("There are {} comparisons using the last element as the pivot "
        "element.".format(comparisons_list[1]))

    print("There are {} comparisons using the median method to determine the "
        "pivot element.".format(comparisons_list[2]))

def setup():
    """Function to import data from the given .txt file"""

    generated_list = []
    
    with open("QuickSort.txt") as f:
        # Exclude the newline character, '\n'
        generated_list = [int(line.rstrip('\n')) for line in f]

    # Update the recursion limit due to how pivots are chosen
    sys.setrecursionlimit(len(generated_list))

    return generated_list

def quicksort(target_list, left_index, right_index, comparisons, pivot_method="random"):
    """Quicksort algorithm, assumes all elements are distinct."""

    # Base case: A difference of 1 or 0 between the left and right
    # indices means the element is sorted and no comparisons are made.
    bounded_list_length = right_index - left_index
    if bounded_list_length < 1:
        return target_list, 0

    pivot_index = select_pivot(target_list, left_index, right_index, 
    pivot_method)
    pivot_value = target_list[pivot_index]

    # Swap the pivot with the element in the leftmost index position
    if pivot_index != left_index:
        target_list = swap(target_list, left_index, pivot_index)

    # Set pointers for partitions
    # i is the pointer for the index where all elements in positions 
    # less than index i are less than the pivot.
    # j is the pointer to the index where all elements in positions 
    # greater than index j have not yet been compared to the pivot.
    i = j = left_index + 1 # The pivot element is in the first position

    while j <= right_index:
        if target_list[j] < pivot_value:
            target_list = swap(target_list, i, j)
            i += 1
        j += 1

    # Swap the pivot element into its rightful position
    target_list = swap(target_list, i-1, left_index)

    # Accumulate the number of comparisons
    comparisons = bounded_list_length - 1

    # Sort the elements less than the pivot
    target_list, low_comparisons = quicksort(target_list, left_index, i-2, comparisons, pivot_method)
    # Sort the elements greater than the pivot
    target_list, high_comparisons = quicksort(target_list, i, len(target_list)-1, comparisons, pivot_method)

    comparisons += low_comparisons + high_comparisons

    return target_list, comparisons

def select_pivot(target_list, left_index, right_index, index_choice):
    """Selects which quicksort pivot method to use."""

    if index_choice == "first":
        # pivot_index = leftmost index position
        pivot_index = left_index
    elif index_choice == "last":
        # pivot_index = rightmost index position
        pivot_index = right_index
    elif index_choice == "median":
        # pivot_index = "median of three"        
        first_element = target_list[left_index]
        last_element = target_list[right_index]

        # Determine the median value of the bounded list
        bounded_list_length = right_index - left_index
        median_index = bounded_list_length//2
        median_element = target_list[median_index]

        potential_median_list = [first_element, median_element, last_element]
        potential_median_list = selection_sort(potential_median_list)
        
        median_of_three = potential_median_list[1]

        if first_element == median_of_three:
            pivot_index = left_index
        elif median_element == median_of_three:
            pivot_index = median_index
        else:
            pivot_index = right_index
    else:
        # random uniform distribution
        pivot_index = randint(left_index, right_index)

    return pivot_index

def swap(L, i, j):
    """Swaps elements i and j in list L."""

    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp

    return L

def selection_sort(given_list):
    """Will always sort 3 elements. Used to determine median value."""

    for i, _ in enumerate(given_list):
        min_value = given_list[i]
        min_index = i
        j = i + 1
        while j < len(given_list):
            if given_list[j] < min_value:
                min_value = given_list[j]
                min_index = j
            j += 1
        given_list = swap(given_list, i, min_index)

    return given_list

if __name__ == "__main__":
    main()