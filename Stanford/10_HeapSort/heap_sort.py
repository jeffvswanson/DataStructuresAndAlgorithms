# heap_sort.py
"""
Example of heapsort implementation using min-heap.

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
    """ Turns the input array into an array resembling a heap."""

    heap = []
    # Heap array is a 1-based index, place a filler at the 0 index.
    heap.append(0)

    for key in A:
        insert(key, heap)


    return heap

def insert(key, heap):
    """Inserts a key into the heap."""

    # The first element, whatever it is, gets put in the parent node.
    if len(heap) < 2:
        heap.append(key)
        return

    heap.append(key)
    
    bubble_up(len(heap), heap)
    
    return

def get_parent(child_index):
    """
    Get the index of the given key's parent given the index 
    of the child key.
    """

    # The root of the tree is at index position 1 
    # and can have no parent
    if child_index == 1:
        return 0
    return child_index // 2

def get_left_child(parent_index, heap):
    """
    Get the index of the left child given the 
    parent node's index.
    """

    # Remember, this is a 1-based index.
    if parent_index * 2 - 1 > len(heap):
        # There is no left child
        return 0

    return parent_index * 2 - 1

def get_right_child(parent_index, heap):
    """
    Get the index of the right child given the
    parent node's index.
    """

    # Remember, this is a 1-based index.
    if parent_index * 2 > len(heap):
        # There is no right child
        return 0
    
    return parent_index * 2

def bubble_up(child_index, heap):
    """Push a child node up through the heap to heap property."""

    parent_index = get_parent(child_index)
    # The node in question is the root node
    if parent_index == 0:
        return

    if heap[child_index] > heap[parent_index]:
        heap[child_index], heap[parent_index] = heap[parent_index], heap[child_index]
        bubble_up(parent_index, heap)
    
    return

def extract_min(heap):
    """Returns the minimum value of the heap, the root."""

    return heap[1]

if __name__ == "__main__":
    main()