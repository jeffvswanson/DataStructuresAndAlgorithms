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

class Heap:
    """
    Heap represents the heap data structure.
    
    Default kind is a min-heap, unless 'max' denoted."""

    def __init__(self, kind="min", *args):

        # Array to start the heap data structure. 
        # Actual nodes start at heap[1] as a heap is a 1-based index.
        # The 0 is a placeholder.
        self.heap = [0]
        self.kind = kind
        for node in args:
            insert(node)

    def insert(self, node):
        """Inserts a node into the heap."""

        # The first element, whatever it is, gets put in the root node
        # position.
        if len(self.heap) < 2:
            if self.kind == "max":
                self.heap.append(-node)
            else: 
                self.heap.append(node)
            return
        
        if self.kind == "max":
            self.heap.append(-node)
        else:
            self.heap.append(node)

        self.bubble_up(len(self.heap)-1)

        return
    
    def bubble_up(self, child_index):
        """
        Push a child node up through the heap to maintain the heap property.
        """

        parent_index = self.get_parent_index(child_index)
        # The node in question is the root node
        if parent_index == 0:
            return

        if self.heap[child_index] < self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = \
                self.heap[parent_index], self.heap[child_index]
            self.bubble_up(parent_index)

        return

    def extract_root(self):
        """
        Extracts and returns the max or min root value of the heap, 
        dependent on heap type.

        Returns True or False if there is a root node to return. That
        is, a heap without a root node (0-element heap) has a return
        value of a 0 and a False.
        """

        # Check if the heap only has the 0-element.
        # False return because there is no root element.
        if self.length() < 1:
            return self.heap[0], False

        if self.kind == "max":
            root = -self.heap[1]
        else:
            root = self.heap[1]

        # Swap the last index position into the root node
        self.heap[1] = self.heap[-1]
        # Pare down the list since the last node became the root
        del self.heap[-1]

        if self.length() > 1:
            self.bubble_down(1)
            
        return root, True

    def bubble_down(self, parent_index):
        """Moves a misplaced node into its appropriate position."""

        min_val = self.heap[parent_index]
        min_index = self.get_left_child_index(parent_index)

        # The parent node has no children
        if min_index == 0:
            return

        # Find the smaller of the two children
        right_child_index = self.get_right_child_index(parent_index)
        if right_child_index == 0:
            right_child_index = min_index
        
        if self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index

        if self.heap[min_index] < min_val:
            min_val = self.heap[min_index]

        if min_val != self.heap[parent_index]:
            self.heap[parent_index], self.heap[min_index] = self.heap[min_index], self.heap[parent_index]
            self.bubble_down(min_index)

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

    def get_left_child_index(self, parent_index):
        """
        Get the index of the left child given the parent
        node's index.
        """

        # Remember this is a 1-base index.
        if parent_index * 2 >= len(self.heap):
            # There is no left-child
            return 0

        return parent_index * 2

    def get_right_child_index(self, parent_index):
        """
        Get the index of the right child given the 
        parent node's index.
        """

        # Remember, this is a 1-base index.
        if parent_index * 2 + 1 >= len(self.heap):
            # There is no right child
            return 0

        return parent_index * 2 + 1

    def peek(self):
        """
        Returns the root of the heap without extracting the root.

        Returns True or False if there is a root node to return. That
        is, a heap without a root node (0-element heap) has a return
        value of a 0 and a False.
        """

        # Check if the heap only has the 0-element.
        # False return because there is no root element.
        if self.length() < 1:
            return self.heap[0], False

        if self.kind == "max":
            root = -self.heap[1]
        else:
            root = self.heap[1]
            
        return root, True

    def length(self):
        """
        Returns the length of the 1-based index heap.
        """

        return len(self.heap) - 1


def main():

    # Used to store highest half of elements
    high_half_heap = Heap()
    # Used to store lowest half of elements
    low_half_heap = Heap("max")

    # even_or_odd tracks whether the count of elements inserted into
    # the heap are even or odd. This should only vary between 0 to 2
    # we don't want the number getting arbitrarily large as the heap
    # grows.
    even_or_odd = 0
    median, median_total = 0, 0
    count = 0

    with open("Median.txt") as f:
        # Exclude the newline character, \n
        for line in f:
            x = int(line.rstrip('\n'))
            count += 1

            # Put x into the correct heap
            # If x > median, place x in high_half_heap
            if x > median:
                high_half_heap.insert(x)
            else:
                low_half_heap.insert(x)
            
            # Check if heaps need to be rebalanced
            rebalance(high_half_heap, low_half_heap)

            # Calculate the median given the new x
            median = find_median(high_half_heap, low_half_heap, count)

            # Add the median to the median_total
            median_total += median
            print("{}.\tmedian = {}\tmedian_total = {}".format(count, median, median_total))
            
    # Once the file is exhausted return_value = median_total%10000
    print("The last four digits of the sums of the medians is {}".format(median_total%10000))

def rebalance(h_high, h_low):
    """
    rebalance prevents one heap from hoarding all the values by 
    keeping the difference in the number of items between each 
    heap less than 2.
    """

    if abs(h_high.length() - h_low.length()) > 1:
                if h_high.length() > h_low.length():
                    root, prs = h_high.extract_root()
                    if prs:
                        h_low.insert(root)
                else:
                    root, prs = h_low.extract_root()
                    if prs:
                        h_high.insert(root)

def find_median(h_high, h_low, count):
    """
    find_median determines the median value between the two heaps.
    """

    # r is the median's index
    r = 0
    if count%2 == 0:
        r = count//2
    else:
        r = (count + 1)//2
        
    if r > h_low.length():
        median, _ = h_high.peek()
    else:
        median, _ = h_low.peek()
        
    return median

if __name__ == "__main__":
    main()