# 2_unimodal_array.py

"""You are given a unimodal array of n distinct elements, meaning that its 
entries are in increasing order up until its maximum element, after which its
elements are in decreasing order. Give an algorithm to compute the maximum
element that runs in O(lg n) time."""

def main():
    A = [1, 3, 5, 7, 9, 8, 6, 0]

    max_element = find_max(A)

    print("The maximum element in the list is {}.".format(max_element))

def find_max(A):
    # Base case: An empty array of array of length 1 is the maximum element.
    if len(A) < 2:
        return A[0]
    
    # Divide
    midpoint = len(A)//2
    # Eliminate decreasing side of the list
    if midpoint + 1 < len(A) and A[midpoint] > A[midpoint + 1]:
        max_element = find_max(A[:midpoint + 1])
    # Eliminate increasing side of the list
    elif midpoint - 1 > -1 and A[midpoint] > A[midpoint - 1]:
        max_element = find_max(A[midpoint:])
    # On the maximum element
    else:
        max_element = A[midpoint]

    return max_element

if __name__ == "__main__":
    main()