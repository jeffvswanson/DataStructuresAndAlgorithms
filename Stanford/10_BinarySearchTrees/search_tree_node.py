# search_tree_node.py

class Node:
    """
    A class used to represent a Node in a red-black search tree.

    Attributes:
        key: The key is the value the node shall be sorted on. The key can be an integer,
            float, string, anything capable of being sorted.
        left: The pointer to the left child node.
        right: The pointer to the right child node.
        color (str): The color attribute keeps track of whether a node is red or black.
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
        self.color = "red"

    def recolor(self):
        """
        Switches the color of a Node from red to black or black to red.
        """

        if self.color == "red":
            self.color = "black"
        elif self.color == "black":
            self.color = "red"

    def set_key(self, key):
        """
        Changes the value of the key.
        """

        self.key = key

    def add_instance(self):
        """
        Allows for duplicates in a node by making it "fat" instead of
        creating more nodes which would defeat the purpose of a self-
        balancing tree.
        """

        self.instance += 1
