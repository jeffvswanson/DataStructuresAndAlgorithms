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

        # Check if there is nothing in the tree
        if self.root == None:
            self.root = new_node
            self.root.recolor()
            return

        # Red-black tree specific
        # If no successor the Node is the root and must be set to black

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
   