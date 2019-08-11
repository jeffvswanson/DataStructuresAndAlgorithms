# red_black_tree.py

import red_black_node as rbn

from typing import Tuple

class RedBlackTree:
    """
    A class used to represent a red-black binary search tree.

    Attributes:


    Methods:
        insert(key: key)
            Inserts an element into the search tree.
        _left_rotation(key)
            Reorganizes a section of the search tree so the parent node, x, 
            becomes the left child of it's original right child, y, and y 
            becomes the parent of x.
        _right_rotation(key)
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
            key: The key of the node you wish to insert.
        """
        
        if key == None:
            return

        new_node = rbn.Node(key)

        # Check if there is nothing in the tree.
        if self.root == None:
            self.root = new_node
            # Paint it black.
            self.root.recolor()
            return

        # Find where the node should be inserted.
        found_node, parent = self.contains(new_node.key)
        
        if found_node != None:
            found_node.add_instance()
        elif new_node.key != parent.key:
            new_node.parent = parent
            if new_node.key < parent.key:
                parent.left = new_node
            else: # new_node.key > parent.key
                parent.right = new_node
            self._rebalance(new_node)

    def _rebalance(self, node):
        """
        Ensures the search tree remains balanced.

        Parameters:
            node: The node where rebalancing should start.
        """

        # Easy case: node's parent is black.
        if node != self.root and not node.parent.is_red:
            return
        
        # Now we have to keep propagating changes up the tree since
        # node's parent is red and there cannot be two reds in a 
        # parent-child relationship.
        while node.parent.is_red and node != self.root:

            grandparent = node.parent.parent

            # Determine the rebalancing case
            if grandparent.right == None or grandparent.left == None:
                self._case2(node)
            elif grandparent.right.is_red and grandparent.left.is_red:
                self._case1(node)
            else:
                self._case2(node)

            # Have to reassign grandparent to to rebalancing
            grandparent = node.parent.parent
            # Do not continue, the root does not have a grandparent.
            if grandparent == self.root or grandparent == None:
                break
            else:
               node = node.parent
        
        # After propagating ensure the root of the tree remains black.
        if self.root.is_red:
            self.root.recolor()

    def _case1(self, node):
        """
        The parent of the node and the parent's sibling are red.

        Leave node as red. The grandparent of red must be black since
        the parent of node is originally red. Color the grandparent of 
        node red and the grandparent's left and right children black.

        Parameters:
            node: The node originating the first case of node reorganization.
        """

        grandparent = node.parent.parent
        grandparent.recolor()

        grandparent.left.recolor()
        grandparent.right.recolor()

    def _case2(self, node):
        """
        The parent of the node is red and the parent's sibling is black or None.

        Rotate node's parent in the opposite direction of node so node
        occupies the original parent's position. Then recolor node and
        node's new parent.

        Parameters:
            node: The node originating the second case of node reorganization.
        """

        grandparent = node.parent.parent
        # Figure out which way to rotate.
        if node.parent == grandparent.right:
            if node == node.parent.right:
                self._left_rotation(grandparent)
                node.parent.recolor()
                node.parent.left.recolor()
            else:
                self._right_rotation(node.parent)
                self._case2(node.right)
        else:
            if node == node.parent.left:
                self._right_rotation(grandparent)
                node.parent.recolor()
                node.parent.right.recolor()
            else:
                self._left_rotation(node.parent)
                self._case2(node.left)

    def _left_rotation(self, node):
        """
        Conducts a left rotation causing the given node to move left down the 
        tree and brings its right child into the vacated position.

          A      left         C
         /\\  ---------->    /
        B   C  rotation     A
                of A       /
                          B

        Parameters:
            node: The parent node to rotate out of position.
        """

        # Adjust the child pointers for the nodes due to the rotation.
        # The node's right child will become the node's parent with 
        # a left rotation
        new_parent = node.right

        # Since the new_parent is greater than node, the new_parent's 
        # left pointer will adjust to point to node and node's right 
        # pointer must be adjusted to point to the soon-to-be orphaned 
        # left node of new_parent.
        node.right = new_parent.left
        if new_parent.left != None:
            new_parent.left.parent = node
        
        # Adjust the parent pointers for the nodes due to the rotation.
        if node.parent == None:
            self.root = new_parent
            # Paint it black
            if self.root.is_red:
                self.root.recolor()
        else:
            new_parent.parent = node.parent
            if node == node.parent.left:
                node.parent.left = new_parent
            else:
                node.parent.right = new_parent

        new_parent.left = node
        node.parent = new_parent

    def _right_rotation(self, node):
        """
        Conducts a right rotation causing the given node to move right down the
        tree and brings its left child into the vacated position. 

          A     right       B
         /\\  ---------->   \\
        B   C  rotation       A
                of A          \\
                                C

        Parameters:
            node: The parent node to rotate out of position.               
        """

        # Adjust the child pointers for the nodes due to the rotation.
        # The node's left child will become the node's parent with
        # a right rotation.
        new_parent = node.left

        # Since the new_parent is less than node, the new_parent's
        # right pointer will adjust to point to node and node's left
        # pointer must be adjusted to point to the soon-to-be orphaned
        # right node of new_parent.
        node.left = new_parent.right
        if new_parent.right != None:
            new_parent.right.parent = node

        # Adjust the parent pointers for the nodes due to the rotation.
        if node.parent == None:
            self.root = new_parent
            # Paint it black
            if self.root.is_red:
                self.root.recolor()
        else:
            new_parent.parent = node.parent
            if node == node.parent.left:
                node.parent.left = new_parent
            else: 
                node.parent.right = new_parent
            
        new_parent.right = node
        node.parent = new_parent

    def delete_instance(self, key):
        """
        Deletes an instance of a node in the red-black search tree. That is, if there
        is more than one instance delete_instance decrements the number of instances
        of the node. If this method is called when only one instance exists the
        delete method gets called to completely remove the node from the search
        tree.

        Parameters:
            key: The key of the node you wish to delete an instance of.
        """

        node, _ = self.contains(key)

        if node == None:
            return
        else:
            node.remove_instance()
            if node.instances < 1:
                self.delete(key)
                if node == self.root:
                    self.root = None

    def delete(self, key):
        """
        Completely removes a node from a red-black search tree regardless of the 
        number of instances the node possesses.

        Parameters:
            key: The key of the node you wish to delete from the search tree.
        """
        
        node, parent = self.contains(key)
        
        if node == None:
            return
        
        # Case 1: node being deleted is red with no children
        if node.is_red and node.left == None and node.right == None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        # Case 2: node is black, node has only one child, and the child is red
        # As a side note, there is no case for a node possessing only one 
        # black child as that would not be a valid tree structure.
        elif node.left != None and node.left.is_red and node.right == None:
            if parent == None:
                self.root = node.left
                self.root.parent == None
                self.root.recolor()
            elif parent.left == node:
                parent.left = node.left
                node.left.parent = parent
                parent.left.recolor()
            else:
                parent.right = node.left
                node.left.parent = parent
                parent.right.recolor()
        elif node.right != None and node.right.is_red and node.left == None:
            if parent == None:
                self.root = node.right
                self.root.parent == None
                self.root.recolor()
            if parent.right == node:
                parent.right = node.right
                node.right.parent = parent
                parent.right.recolor()
            else:
                parent.left = node.right
                node.right.parent = parent
                parent.left.recolor()
        # Case 3: node is black
        else:
            self._case3(node)
            if parent != None:
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
        
        node.delete()

    def _case3(self, node):
        """
        Case 3 occurs when the node we want to delete is a black node.

        Since deleting a black node would alter the requirement to have
        the same number of black nodes regardless of the path taken
        the tree must be adjusted.

        Parameters:
            node: The node originating the case 3 deletion.
        """

        # node is the root and does not need case 3.
        if node.parent == None:
            return

        parent = node.parent

        if parent.right == node:
            s = parent.left
        else: 
            s = parent.right
        # Case 3.1: node's sibling, s, is red
        if s.is_red:
            parent.recolor()
            s.recolor()
            if s == parent.left:
                self._right_rotation(parent)
            else:
                self._left_rotation(parent)
            self._case3(node)
        else: # node's sibling, s, is black
            # Case 3.2: Both children of s are black
            if not ((s.left != None and s.left.is_red) and (s.right != None and s.right.is_red)):
                s.recolor() # s is now red
                if parent.is_red:
                    parent.recolor()
                    return
                else:
                    # Defaults to case 3.1 on the next pass-through.
                    self._case3(node)

            # Case 3.3: s's left child is red
            elif s.left.is_red and not s.right.is_red:
                s.recolor() # s is red
                s.left.is_red.recolor() # s.left is black
                self._right_rotation(s) # sets us up for case 3.4

            # Case 3.4: s's right child is red
            if s.right.is_red:
                s.right.recolor() # s.right is black
                if parent.is_red:
                    s.parent.recolor() # s.parent is black
                self._left_rotation(s.parent)

    def traverse(self, node) -> list:
        """
        Provides keys in increasing order.

        Parameters:
            node: The node the in-order traversal will start from.

        Returns:
            list: A list of the tree's keys in ascending order.
        """
        
        tree = []
        if node != None:
            tree = self.traverse(node.left)
            tree.append(node.key)
            tree = tree + self.traverse(node.right)

        return tree

    def successor(self, key=None) -> rbn.Node:
        """
        Computes the next greater value in the search tree. If no successor is found,
        the key is a maximum.

        Returns: 
            node.key: The successor node's value.
        """

        # Easy Case: If the key in question's right subtree is not empty, 
        # return the min key in the right subtree.
        key_node = self.contains(key)[0]
        if key_node != None and key_node.right != None:
            return self.min(key_node.right)

        # Otherwise, Follow parent pointers of the key in question until you
        # get to a key value greater than the original key. If you reach the 
        # root and have not found a key greater than the original key, then
        # there is no successor in the search tree and the original key is 
        # the maximum key.
        succ = key_node
        while succ.parent != None:
            if succ.parent == self.root and self.root.key < key_node.key:
                return None
            elif succ.parent.key > key_node.key:
                return succ.parent
            succ = succ.parent
        

    def predecessor(self, key=None) -> rbn.Node:
        """
        Computes the next least value in the search tree. If no predecessor is found,
        the key is a minimum.

        Returns:
            node.key: The predecessor node's value.
        """

        # Easy Case: If the key in question's left subtree is not empty, return 
        # the max key in the left subtree.
        key_node = self.contains(key)[0]
        if key_node != None and key_node.left != None:
            return self.min(key_node.left)

        # Otherwise: Follow parent pointers of the key in question until you 
        # get to a key value less than the original key. If you reach the root
        # and have not found a key less than the original key, then there is 
        # no predecessor in the search tree and the original key is the 
        # minimum key.
        pred = key_node
        while pred.parent != None:
            if pred.parent == self.root and self.root.key > key_node.key:
                return None
            elif pred.parent.key < key_node.key:
                return pred.parent
            pred = pred.parent

    def max(self) -> rbn.Node:
        """
        Computes the maximum value in the search tree.

        Returns:
            node.key: The maximum node's value.
        """

        max_node = self.root

        if max_node != None:
            while max_node.right != None:
                max_node = max_node.right

        return max_node

    def min(self, min_node=None) -> rbn.Node:
        """
        Computes the minimum value in the search tree.

        Returns:
            node.key: The minimum node's value.
        """

        # Working with predecessor, have the min function take as default a None node parameter
        # If the node is none assign it as the root in the min
        # Then we can do a min search from the node or continue on

        if min_node == None:
            min_node = self.root

        
        while min_node != None and min_node.left != None:
            min_node = min_node.left

        return min_node

    def contains(self, v) -> Tuple[rbn.Node, rbn.Node]:
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
            if current_node.key != None and v < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node == self.root:
            parent = None

        return current_node, parent
   