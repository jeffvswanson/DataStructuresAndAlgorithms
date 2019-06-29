# 1_unsorted_array.py

"""You are given as input an unsorted array of n distinct numbers, where n is 
a power of 2. Give an algorithm that identifies the second-largest number in
the array, and that uses at most n + lg n - 2 comparisons."""

from random import randint

def main():
    n = 32
    A = []
    for _ in range(n):
        A.append(randint(0, n**2))
    
    print("The unsorted array is", A)

    A = divide_and_conquer(A)

    print("The second larget number in the list is {}.".format(A[-2]))

def divide_and_conquer(A):
    # Base case: if a list is empty or is one element long the list, 
    # by default, is sorted.
    if len(A) < 2:
        return A

    midpoint = len(A)//2
    # Divide
    a = divide_and_conquer(A[0:midpoint])
    b = divide_and_conquer(A[midpoint:])

    # Combine
    sorted_list = combine(a, b)

    return sorted_list

def combine(a, b):
    sorted_list = []
    i = j = 0

    for _ in range(len(a) + len(b)):
        # Check if we've run out of elements in a or b or we'll have an error.
        if i >= len(a):
            while j < len(b):
                sorted_list.append(b[j])
                j += 1
            break
        elif j >= len(b):
            while i < len(a):
                sorted_list.append(a[i])
                i += 1
            break

        # Combine lists
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    return sorted_list

if __name__ == "__main__":
    main()