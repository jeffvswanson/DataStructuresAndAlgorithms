# heap_median_maintenance.py
"""
With the following text file: Median.txt

The goal of this problem is to implement the "Median Maintenance" 
algorithm (covered in the Week 5 lecture on heap applications). The 
text file contains a list of the integers from 1 to 10000 in 
unsorted order; you should treat this as a stream of numbers, arriving
one by one. Letting x-subscript i denote the i-th number of the file, 
the k-th median m-subscript k is defined as the median of the numbers 
x-subscript 1,..., x-subscript k. (So, if k is odd, then m-subscript k 
is ((k+1)/2)th smallest number among x-subscript 1,...,x-subscript k; 
if k is even, then m-subscript k is the (k/2)th smallest number among
x-subscript 1,...,x-subscript k.)

Find the sum of these 10000 medians, modulo 10000 
(i.e., only the last 4 digits). That is, you should compute
(m-subscript 1 + m-subscript 2 + ... + m-subscript 10000) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and 
search-tree-based implementations of the algorithm.
"""

class Node:
    """Node represents where a value goes in the heap"""

    def __init__(self, value):
        self.node = value

    def get_parent_index(self, child_index):
        """
        Get the index of the given node's parent given the index 
        of the child node.
        """

        # The root of the tree is at index position 1 
        # and can have no parent
        if child_index == 1:
            return 0
        return child_index // 2

    def get_left_child_index(self, parent_index, heap):
        """
        Get the index of the left child given the parent
        node's index.
        """

        # Remember this is a 1-base index.
        if parent_index * 2 >= len(heap):
            # There is no left-child
            return 0

        return parent_index * 2

    def get_right_child_index(self, parent_index, heap):
        """
        Get the index of the right childe given the 
        parent node's index.
        """

        # Remember, this is a 1-base index.
        if parent_index * 2 + 1 >= len(heap):
            # There is no right child
            return 0

        return parent_index * 2 + 1

class Heap:
    """Heap represents the heap data structure."""

    def __init__(self, *args):

        # Array to start the heap data structure. 
        # Actual nodes start at heap[1] as a heap is a 1-based index.
        # The 0 is a placeholder.
        self.heap = [0]
        for node in args:
            insert(node)

    def insert(self, node):
        """Inserts a node into the heap."""

        # The first element, whatever it is, gets put in the root node
        # position.
        if len(self.heap) < 2:
            self.heap.append(node)
            return
        
        self.heap.append(node)

        bubble_up(len(self.heap)-1)

        return
    
    def bubble_up(self, child_index):
        """
        Push a child node up through the heap to maintain the heap property.
        """

        parent_index = Node.get_parent_index(child_index, self.heap)
        # The node in question is the root node
        if parent_index == 0:
            return

        if self.heap[child_index] < self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = \
                self.heap[parent_index], self.heap[child_index]
            bubble_up(parent_index)

        return

    def extract_min(self):
        """Returns the minimum value of the heap, the root."""

        # Check if the heap only has the 0-element.
        if len(self.heap) < 2:
            return self.heap[0], self.heap

        root = self.heap[1]
        # Swap the last index position into the root node
        self.heap[1] = self.heap[-1]
        # Pare down the list since the last node became the root
        del self.heap[-1]

        if len(self.heap) > 1:
            bubble_down(1)

        return root

    def bubble_down(self, parent_index):
        """Moves a misplaced node into its appropriate position."""

        min_val = self.heap[parent_index]
        min_index = Node.get_left_child_index(parent_index, self.heap)

        # The parent node has no children
        if min_index == 0:
            return

        # Find the smaller of the two children
        right_child_index = Node.get_right_child_index(parent_index, self.heap)
        if right_child_index == 0:
            right_child_index = min_index
        
        if self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index

        if self.heap[min_index] < min_val:
            min_val = self.heap[min_index]

        if min_val != self.heap[parent_index]:
            self.heap[parent_index], self.heap[min_index] = self.heap[min_index], self.heap[parent_index]
            bubble_down(min_index)

def main():

    min_heap = Heap()
    max_heap = Heap()

    print(type(min_heap))
    print(len(max_heap.heap))

    max_heap.insert(1)

    print(len(max_heap.heap))

if __name__ == "__main__":
    main()