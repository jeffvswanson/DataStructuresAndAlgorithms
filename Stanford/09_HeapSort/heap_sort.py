# heap_sort.py
"""
Example of heapsort implementation using min-heap.

Demonstrates insertion into a heap data structure and extract minimum 
value from the heap.
"""

def main():
    A = [11, 13, 9, 4, 12, 9, 4, 8, 4]
    print("Original list: {}".format(A))

    # Create the heap
    heap = heapify(A)

    print("List after heapifying: {}".format(heap))

    sorted_list = []
    # Sort the original list
    while len(heap) > 1:
        min_value, heap = extract_min(heap)
        sorted_list.append(min_value)

    print("The sorted list using heapsort is:")
    print(sorted_list)

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
    
    bubble_up(len(heap)-1, heap)
    
    return

def get_parent_index(child_index):
    """
    Get the index of the given key's parent given the index 
    of the child key.
    """

    # The root of the tree is at index position 1 
    # and can have no parent
    if child_index == 1:
        return 0
    return child_index // 2

def get_left_child_index(parent_index, heap):
    """
    Get the index of the left child given the 
    parent node's index.
    """

    # Remember, this is a 1-based index.
    if parent_index * 2 >= len(heap):
        # There is no left child
        return 0

    return parent_index * 2

def get_right_child_index(parent_index, heap):
    """
    Get the index of the right child given the
    parent node's index.
    """

    # Remember, this is a 1-based index.
    if parent_index * 2 + 1 >= len(heap):
        # There is no right child
        return 0
    
    return parent_index * 2 + 1

def bubble_up(child_index, heap):
    """
    Push a child node up through the heap to maintain heap property.
    """

    parent_index = get_parent_index(child_index)
    # The node in question is the root node
    if parent_index == 0:
        return

    if heap[child_index] < heap[parent_index]:
        heap[child_index], heap[parent_index] = heap[parent_index], heap[child_index]
        bubble_up(parent_index, heap)
    
    return

def extract_min(heap):
    """Returns the minimum value of the heap, the root."""

    # Check if the heap only has the 0-element
    if len(heap) < 2:
        return heap[0], heap

    root = heap[1]
    # Swap the last index position into the root node
    heap[1] = heap[-1]
    # Pare down the list since the last node became the root
    del heap[-1]
    
    if len(heap) > 1:
        bubble_down(1, heap)

    return root, heap

def bubble_down(parent_index, heap):
    """Moves a misplaced node into its appropriate position."""
    
    min_val = heap[parent_index]
    min_index = get_left_child_index(parent_index, heap)
    
    # The parent node has no children
    if min_index == 0:
        return

    # Find the smaller of the two children
    right_child_index = get_right_child_index(parent_index, heap)
    if right_child_index == 0:
        right_child_index = min_index

    if heap[right_child_index] < heap[min_index]:
        min_index = right_child_index

    if heap[min_index] < min_val:
        min_val = heap[min_index]

    if min_val != heap[parent_index]:
        heap[parent_index], heap[min_index] = heap[min_index], heap[parent_index]
        bubble_down(min_index, heap)

if __name__ == "__main__":
    main()