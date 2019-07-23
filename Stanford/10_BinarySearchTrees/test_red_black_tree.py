# test_red_black_tree.py

import unittest

import red_black_tree as rb
import search_tree_node as stn

class TestRedBlackBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = rb.RedBlackTree()

    def test_contains(self):

        search_value = stn.Node(0)

        # Test for match
        self.tree.root = stn.Node(0)
        got = self.tree.contains(search_value.key)
        want = (search_value.key, search_value.key)
        self.assertTupleEqual((got[0].key, got[1].key), want)

        # Test for value less than comparison node, also tests no match
        self.tree.root = stn.Node(1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertEqual((got[0], got[1].key), want)

        # Test for value greater than comparison node
        self.tree.root = stn.Node(-1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertTupleEqual((got[0], got[1].key), want)

    def test_insert_empty_tree(self):

        self.tree.insert(1)
        want = stn.Node(1)
        want.recolor()
        self.assertEqual(self.tree.root.key, want.key, "initialized root has incorrect key value")
        self.assertEqual(self.tree.root.instances, want.instances, "initialized root has incorrect number of instances")
        self.assertEqual(self.tree.root.parent, want.parent, "root parent not None")
        self.assertEqual(self.tree.root.left, want.left, "root node's left child not None")
        self.assertEqual(self.tree.root.right, want.right, "root node's right child not None")
        self.assertEqual(self.tree.root.is_red, want.is_red, "root node not colored black")


    def test_max(self):

        # Test for max in empty tree
        # Test for max with only root node
        # Test for max with all values less than root node
        # Test for max with all values greater than root node
        # Test for max in tree with values less than and greater than root node
        pass

    def test_min(self):

        # Test for min in empty tree
        # Test for min with only root node
        # Test for min with all values less than root node
        # Test for min with all values greater than root node
        # Test for min in tree with values less than and greater than root node
        pass

    def test_left_rotation(self):

        # Test for new_parent with empty left subtree
        # Test for new_parent with non-empty left subtree
        # Test for original node as root
        # Test for original node as non-root and a left child
        # Test for original node as non-root and a right child
        pass

    def test_right_rotation(self):

        # Test for new_parent with empty right subtree
        # Test for new_parent with non-empty right subtree
        # Test for original node as root
        # Test for original node as non-root and a left child
        # Test for original node as non-root and a right child
        pass

    def test_rebalance(self):
        pass

    def test_insert(self):

        # Test insert to an empty tree
        # Test insert value less than root
        # Test insert value greater than root
        # Test insert duplicate value
        pass

    def test_case1(self):

        # Test to ensure colors get changed, not worried about red-black
        # maintenance
        pass

    def test_case2(self):

        # Test to ensure rotations occur and colors are changes, not
        # worried about red-black maintenance
        pass

    def test_traverse(self):

        # Test default with root node traversal
        # Test a subtree traversal, that is, not starting at root node
        pass

    def test_successor(self):

        # Test easy case
        # Test other case
        # Test key not in search tree
        pass

    def test_predecessor(self):

        # Test easy case
        # Test other case
        # Test key not in search tree
        pass

if __name__ == "__main__":
    unittest.main()