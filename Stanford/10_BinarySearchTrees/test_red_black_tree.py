# test_red_black_tree.py

import unittest

import red_black_tree as rb
import red_black_node as rbn

class TestRedBlackBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = rb.RedBlackTree()

    def test_contains(self):

        search_value = rbn.Node(0)

        # Test for match
        self.tree.root = rbn.Node(0)
        got = self.tree.contains(search_value.key)
        want = (search_value.key, search_value.key)
        self.assertTupleEqual((got[0].key, got[1].key), want)

        # Test for value less than comparison node, also tests no match
        self.tree.root = rbn.Node(1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertEqual((got[0], got[1].key), want)

        # Test for value greater than comparison node
        self.tree.root = rbn.Node(-1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertTupleEqual((got[0], got[1].key), want)

    def test_max(self):

        # Test for max in empty tree
        got = self.tree.max()
        want = None
        self.assertEqual(got, want, "max failed on empty tree, should be None")

        # Test for max with only root node
        self.tree.insert(0)
        got = self.tree.max()
        want = 0
        self.assertEqual(got.key, want, "max failed with only root node")

        # Test for max with all values less than root node
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.max()
        self.assertEqual(got.key, want, "max failed with all values less than root node")

        # Test for max with all values greater than root node
        self.tree = rb.RedBlackTree()
        self.tree.insert(0)
        self.tree.insert(1)
        self.tree.insert(2)
        got = self.tree.max()
        want = 2
        self.assertEqual(got.key, want, "max failed with all values greater than root node")

        # Test for max in tree with values less than and greater than root node
        self.tree.insert(-1)
        self.tree.insert(-2)
        self.tree.insert(3)
        got = self.tree.max()
        want = 3
        self.assertEqual(got.key, want, "max failed with values greater and less than root node")

    def test_min(self):

        # Test for min in empty tree
        got = self.tree.min()
        want = None
        self.assertEqual(got, want, "min failed on empty tree, should be None")

        # Test for min with only root node
        self.tree.insert(0)
        got = self.tree.min()
        want = 0
        self.assertEqual(got.key, want, "min failed with only root node")

        # Test for min with all values less than root node
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.min()
        want = -2
        self.assertEqual(got.key, want, "min failed with all values less than original root node")

        # Test for min with all values greater than root node
        self.tree = rb.RedBlackTree()
        self.tree.insert(0)
        self.tree.insert(1)
        self.tree.insert(2)
        got = self.tree.min()
        want = 0
        self.assertEqual(got.key, want, "min failed with all values greater than original root node")

        # Test for min in tree with values less than and greater than root node
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.min()
        want = -2
        self.assertEqual(got.key, want, "min failed with values greater and less than original root node")

    def test_left_rotation(self):

        # Test for left rotation by inserting two values greater than root node
        self.tree.insert(0)
        self.tree.insert(1)
        self.tree.insert(2)
        got = self.tree.root
        want = 1
        self.assertEqual(got.key, want, "_left_rotation failed, root incorrect")
        self.assertFalse(got.is_red, "_left_rotation failed to recolor root to black")
        self.assertTrue(got.right.is_red, "_left_rotation failed, right child not red")
        self.assertTrue(got.left.is_red, "_left_rotation failed, left child not red")

    def test_right_rotation(self):

        # Test for right rotation by inserting two values less than root node
        self.tree.insert(0)
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.root
        want = -1
        self.assertEqual(got.key, want, "_right_rotation failed, root incorrect")
        self.assertFalse(got.is_red, "_right_rotation failed to recolor root to black")
        self.assertTrue(got.right.is_red, "_right rotation failed, right child not red")
        self.assertTrue(got.left.is_red, "_right_rotation failed, left child not red")

    def test_rebalance(self):
        
        # Test that node is not root and node's parent is black
        # self.tree.insert(0)
        # self.tree.insert(-1)
        # got = self.tree.root.left
        # want = stn.Node()

    def test_insert(self):

        # Test insert to an empty tree
        self.tree.insert(0)
        want = rbn.Node(0)
        want.recolor()
        self.assertEqual(self.tree.root.key, want.key, "insert into empty tree failed, keys not equal")
        self.assertEqual(self.tree.root.instances, want.instances, "insert into empty tree failed, instances not equal")
        self.assertEqual(self.tree.root.parent, want.parent, "insert in to empty tree failed, parent pointers not equal")
        self.assertEqual(self.tree.root.left, want.left, "insert into empty tree failed, left child should be None")
        self.assertEqual(self.tree.root.right, want.right, "insert into empty tree failed, right child should be None")
        self.assertFalse(self.tree.root.is_red, "insert root into empty tree failed, root should be black not red")

        # Test insert value less than root
        self.tree.insert(-1)
        self.assertEqual(self.tree.root.left.key, -1, "inserting a smaller element into the tree failed")
        self.assertEqual(self.tree.root.key, self.tree.root.left.parent.key, "left child's parent not correct")

        # Test insert value greater than root
        self.tree.insert(1)
        self.assertEqual(self.tree.root.right.key, 1, "inserting a larger element into the tree failed")
        self.assertEqual(self.tree.root.key, self.tree.root.right.parent.key, "right child's parent not correct")

        # Test insert duplicate value
        self.tree.insert(1)
        want = 2
        self.assertEqual(self.tree.root.right.instances, want, "inserting a duplicate value failed")

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

    def test_delete_instance(self):

        # Test no nodes in tree
        # Test removing one instance
        # Test removing a second instance
        # Test removing a node so the instances go to 0
        pass

    def test_delete(self):

        # Test no nodes in tree
        # Test removing a node for each case
        pass

if __name__ == "__main__":
    unittest.main()