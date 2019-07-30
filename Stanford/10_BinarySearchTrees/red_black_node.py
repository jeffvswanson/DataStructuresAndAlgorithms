# red_black_node.py

class Node:
    """
    A class used to represent a Node in a red-black search tree.

    Attributes:
        key: The key is the value the node shall be sorted on. The key can be an integer,
            float, string, anything capable of being sorted.
        instances (int): The number of times the key for a node was inserted into the tree.
        parent (node): The pointer to the parent of the node.
        left (node): The pointer to the left child node.
        right (node): The pointer to the right child node.
        is_red (bool): The color attribute keeps track of whether a node is red or black.
    """

    def __init__(self, key):
        """
        Parameters:
            key: The key is the value the node shall be sorted on. The key can be an integer,
                float, string, anything capable of being sorted. 
        """

        self.key = key
        self.instances = 1
        self.parent = None
        self.left = None
        self.right = None
        self.is_red = True

    def recolor(self):
        """
        Switches the color of a Node from red to black or black to red.
        """

        if self.is_red:
            self.is_red = False
        else:
            self.is_red = True

    def add_instance(self):
        """
        Allows for duplicates in a node by making it "fat" instead of
        creating more nodes which would defeat the purpose of a self-
        balancing tree.
        """

        self.instances += 1

    def remove_instance(self):
        """
        Allows for removal of a single instance of a key from the
        search tree rather than pruning an entire node from the tree.
        """

        self.instances -= 1

    def delete(self):
        """
        Zeroes out a node for deletion.
        """

        self.key = None
        self.instances = 0
        self.parent = None
        self.left = None
        self.right = None
        self.is_red = True