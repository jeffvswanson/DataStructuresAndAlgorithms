# heap_sort.py
"""
Example of heapsort implementation.

Demonstrates insertion into a heap data structure and extract minimum 
value from the heap.
"""

def main():
    A = [11, 13, 9, 4, 12, 9, 4, 8, 4]

    # Create the heap
    heap = heapify(A)

    # Sort the original list
    for idx, _ in enumerate(A):
        A[idx] = extract_min(heap)

    print("The sorted list using heapsort is:")
    print(A)

def heapify(A):

    heap = []
    for key in A:
        heap.append(insert(key))

    return heap

def insert(key):
    """Inserts a key at the last position in the heap."""

    pass

def extract_min():
    """Returns the minimum value of the heap, the root."""

    pass 

if __name__ == "__main__":
    main()