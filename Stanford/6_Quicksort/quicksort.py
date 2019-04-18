# quicksort.py
# A program to show how to implement quicksort in an average of O(n lg n)
# runtime.

from random import randint

def main():
    target_list = [0, 7, 1, 2, 5, 8, 6, 3, 9, 4]
    
    print("The initial unsorted list is:\t", target_list)

    target_list = quicksort(target_list, 0, len(target_list)-1)

    print("The quicksorted list is:\t", target_list)

def quicksort(input_list, left_index, right_index):
    # Base case: A difference of 1 or 0 between the left and right index means 
    # the element is sorted.
    if right_index - left_index < 1:
        return input_list

    pivot_index = randint(left_index, right_index)
    pivot = input_list[pivot_index]

    # Swap the pivot element with the element in the leftmost index position
    input_list = swap(input_list, left_index, pivot_index)

    # Set pointers for partitions
    # i is the pointer for the index where all elements in positions less than
    # index i are less than the pivot.
    # j is the pointer to the index where all elements in positions greater than
    # index j have not yet been compared to the pivot.
    i = j = left_index + 1 # The pivot element is in the first position

    while j <= right_index:
        if input_list[j] <= pivot:
            input_list = swap(input_list, i, j)
            i += 1
        j += 1

    # Swap the pivot element into its rightful position
    input_list = swap(input_list, i-1, left_index)

    # Sort the elements less than the pivot
    input_list = quicksort(input_list, left_index, i-2)
    # Sort the elements greater than the pivot
    input_list = quicksort(input_list, i, len(input_list)-1)

    return input_list

def swap(L, i, j):
    # Swap the elements at i and j in the list, L.
    tmp = L[i]
    L[i] = L[j]
    L[j] = tmp

    return L

if __name__ == "__main__":
    main()