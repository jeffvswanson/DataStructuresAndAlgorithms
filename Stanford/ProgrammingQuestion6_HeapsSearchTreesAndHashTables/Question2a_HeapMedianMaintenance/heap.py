# heap.py

class Node:
    """Node represents where a value goes in the heap"""

    def __init__(self, value):
        self.node = value

class Heap:
    """
    Heap represents the heap data structure.
    
    Default heap kind is a min-heap, unless 'max' denoted.
    """

    def __init__(self, kind="min", *args):

        # Array to start the heap data structure. 
        # Actual nodes start at heap[1] as a heap is a 1-based index.
        # The 0 is a placeholder.
        self.heap = [0]
        self.kind = kind
        for node in args:
            self.insert(node)

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
            return False
        return child_index // 2

    def get_left_child_index(self, parent_index):
        """
        Get the index of the left child given the parent
        node's index.
        """

        # Remember this is a 1-base index.
        if parent_index * 2 > self.length():
            # There is no left-child
            return False

        return parent_index * 2

    def get_right_child_index(self, parent_index):
        """
        Get the index of the right child given the 
        parent node's index.
        """

        # Remember, this is a 1-base index.
        if parent_index * 2 + 1 > self.length():
            # There is no right child
            return False

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