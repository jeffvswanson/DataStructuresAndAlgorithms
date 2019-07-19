# red_black_tree.py

import search_tree_node as stn

from typing import Tuple

class RedBlackTree:
    """
    A class used to represent a red-black binary search tree.

    Attributes:


    Methods:
        insert(key: key)
            Inserts an element into the search tree.
        left_rotation(key)
            Reorganizes a section of the search tree so the parent node, x, 
            becomes the left child of it's original right child, y, and y 
            becomes the parent of x.
        right_rotation(key)
            Reorganizes a section of the search tree so the parent node, x,
            becomes the right child of its original left child, y, and y
            becomes the parent of x.
        recolor(key)
            Recolors nodes starting at the key to ensure the red-black tree 
            invariants are maintained when a change to the search tree occurs.
        delete(key)
            Deletes a node from the search tree if the key exists.
        traverse() -> list
            Prints the keys of the search tree in ascending order, for example,
            1, 2, 3, 4, ..., n.
        successor(key: key) -> key
            Provides the given key's closest node in value that is greater than
            the key if it exists in the search tree.
        predecessor(key: key) -> key
            Provides the given key's closest node in value that is less than the
            key if it exists in the search tree.
        max() -> key
            Provides the maximum value that exists in the search tree.
        min() -> key
            Provides the minimum vlaue that exists in the search tree.
        contains(key) -> Tuple[key, bool]
            Checks if a value exists in the search tree.
    """

    def __init__(self):
        """
        Parameters:
            None
        """

        self.root = None

    def insert(self, key):
        """
        Inserts a node into the search tree.

        Parameters:
            key: The key of the node you wish to insert
        """
        
        new_node = stn.Node(key)

        # Check if there is nothing in the tree.
        if self.root == None:
            self.root = new_node
            # Paint it black.
            self.root.recolor()
            return

        # Find where the node should be inserted.
        found_node, parent = self.contains(new_node.key)
        
        if new_node.key != parent.key:
            if new_node.key < parent.key:
                parent.left = new_node
            else: # new_node.key > parent.key
                parent.right = new_node
            self.rebalance(new_node)
        else:
            found_node.add_instance()

    def rebalance(self, node):
        """
        Ensures the search tree remains balanced.
        """

        pass    

    def left_rotation(self, node):
        """
        Conducts a left rotation causing the given node to move left down the 
        tree and brings its right child into the vacated position.

          A      left         C
         /\\  ---------->    /
        B   C  rotation     A
                of A       /
                          B               
        """

        # Adjust the pointers for the nodes.
        new_parent = node.right


    def right_rotation(self, node):
        """
        Conducts a right rotation causing the given node to move right down the
        tree and brings its left child into the vacated position. 

          A     right       B
         /\\  ---------->   \\
        B   C  rotation       A
                of A          \\
                                C                                   
        """

        pass

    def delete(self, key):
        """
        """

        pass

    def traverse(self):
        """
        Prints keys in increasing order.
        """
        
        pass

    def successor(self, key):
        """
        Computes the next greater value in the search tree. If no successor is found,
        the key is a maximum.

        Returns: 
            node.key: The successor node's value.
        """

        pass

    def predecessor(self, key):
        """
        Computes the next least value in the search tree. If no predecessor is found,
        the key is a minimum.

        Returns:
            node.key: The predecessor node's value.
        """

        pass

    def max(self) -> stn.Node.key:
        """
        Computes the maximum value in the search tree.

        Returns:
            node.key: The maximum node's value.
        """

        max_node = self.root

        while max_node != None:
            max_node = max_node.right

        return max_node.key

    def min(self) -> stn.Node.key:
        """
        Computes the minimum value in the search tree.

        Returns:
            node.key: The minimum node's value.
        """

        min_node = self.root

        while min_node != None:
            min_node = min_node.left

        return min_node.key

    def contains(self, v) -> Tuple[stn.Node, stn.Node]:
        """
        Checks if the given value is in the search tree. It returns the 
        last node accessed

        Parameters:
            v: The value you wish to check for.

        Returns:
            node: The node the search ended on whether a null node or 
                an actual node.
            node: The last node accessed (parent or potential parent).
        """

        current_node, parent = self.root, self.root

        while current_node != None and v != current_node.key:
            parent = current_node
            if v < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right   

        return current_node, parent
   