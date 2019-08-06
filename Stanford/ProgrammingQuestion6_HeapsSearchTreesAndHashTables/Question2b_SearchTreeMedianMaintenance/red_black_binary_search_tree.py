# red_black_binary_search_tree.py

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

    def insert(self, key: key):
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

    def left_rotation(self, key: key):
        """
        """

        pass

    def right_rotation(self, key: key):
        """
        """

        pass

    def delete(self, key: key):
        """
        """

        pass

    def traverse(self):
        """
        """
        
        pass

    def successor(self, key: key) -> key:
        """
        """

        pass

    def predecessor(self, key: key) -> key:
        """
        """

        pass

    def max(self) -> key:
        """
        """

        pass

    def min(self) -> key:
        """
        """

        pass

    def contains(self, v, k: Node.key) -> Tuple[key, bool]:
        """
        Checks if the given value is in the search tree.

        Parameters:
            v: The value you wish to check for.
            k: The key of a comparison node.

        Returns:
            key: The value of the key if the search tree contains it, otherwise 0.
            bool: True if the search tree contains key, otherwise False.
        """

        # Start at the root
        # Traverse left/right child pointers as needed. That is:
            # if k < Node.key compared go left
            # else go right
        # Return node with k or null (k is not in the search tree) as appropriate

        # if k == None:
            # return None, False
        # if v < k:
            # contains(v, Node.left)
        # elif v > k:
            # contains(v, Node.right)
        # else:
            # return v, True

class Node:
    """
    A class used to represent a Node in a red-black search tree.

    Attributes:
        key: The key is the value the node shall be sorted on. The key can be an integer,
            float, string, anything capable of being sorted.
        color (str): The color attribute records whether a node is red or black.
    """

    def __init__(self, key):
        """
        Parameters:
            key: The key is the value the node shall be sorted on. The key can be an integer,
                float, string, anything capable of being sorted. 
            left: The pointer to the left child node.
            right: The pointer to the right child node.
            color (str): The color attribute keeps track of whether a node is red or black.
        """

        self.key = key
        self.left = None
        self.right = None
        self.color = "red"

    def setColor(self):
        """
        Sets the color of a Node.
        """

        pass

        







        