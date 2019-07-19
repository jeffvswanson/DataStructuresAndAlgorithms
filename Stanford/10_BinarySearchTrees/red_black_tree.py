# red_black_binary_search_tree.py

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

        self.root = stn.Node(None)

    def insert(self, key):
        """
        Inserts a node into the search tree.

        Parameters:
            key : key
                The key of the node you wish to insert
        """
        
        # Search for a node with the value of key in the search tree 

        # Red-black tree specific
        # If no successor the Node is the root and must be set to black
        pass

    def left_rotation(self, key):
        """
        """

        pass

    def right_rotation(self, key):
        """
        """

        pass

    def delete(self, key):
        """
        """

        pass

    def traverse(self):
        """
        """
        
        pass

    def successor(self, key):
        """
        """

        pass

    def predecessor(self, key):
        """
        """

        pass

    def max(self):
        """
        """

        pass

    def min(self):
        """
        """

        pass

    def contains(self, v, n):
        """
        Checks if the given value is in the search tree.

        Parameters:
            v: The value you wish to check for.
            n: The comparison node.

        Returns:
            key: The value of the key if the search tree contains it, otherwise 0.
            bool: True if the search tree contains key, otherwise False.
        """

        if n == None or n.key == None:
            return None, False
        if v < n.key:
            return self.contains(v, n.left)
        elif v > n.key:
            return self.contains(v, n.right)
        else:
            return v, True
   