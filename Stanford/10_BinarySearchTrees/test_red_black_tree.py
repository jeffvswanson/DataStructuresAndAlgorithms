# test_red_black_tree.py

import unittest

import red_black_tree as rb
import red_black_node as rbn

class TestRedBlackBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = rb.RedBlackTree()

    def test_contains(self):

        search_value = rbn.Node(0)

        # Test for match.
        self.tree.root = rbn.Node(0)
        got = self.tree.contains(search_value.key)
        want = (search_value.key, None)
        self.assertTupleEqual((got[0].key, got[1]), want)

        # Test for value less than comparison node, also tests no match.
        self.tree.root = rbn.Node(1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertEqual((got[0], got[1].key), want)

        # Test for value greater than comparison node.
        self.tree.root = rbn.Node(-1)
        got = self.tree.contains(search_value.key)
        want = (None, self.tree.root.key)
        self.assertTupleEqual((got[0], got[1].key), want)

    def test_max(self):

        # Test for max in empty tree.
        got = self.tree.max()
        want = None
        self.assertEqual(got, want, "max failed on empty tree, should be None")

        # Test for max with only root node.
        self.tree.insert(0)
        got = self.tree.max()
        want = 0
        self.assertEqual(got.key, want, "max failed with only root node")

        # Test for max with all values less than root node.
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.max()
        self.assertEqual(got.key, want, "max failed with all values less than root node")

        # Test for max with all values greater than root node.
        self.tree = rb.RedBlackTree()
        self.tree.insert(0)
        self.tree.insert(1)
        self.tree.insert(2)
        got = self.tree.max()
        want = 2
        self.assertEqual(got.key, want, "max failed with all values greater than root node")

        # Test for max in tree with values less than and greater than root node.
        self.tree.insert(-1)
        self.tree.insert(-2)
        self.tree.insert(3)
        got = self.tree.max()
        want = 3
        self.assertEqual(got.key, want, "max failed with values greater and less than root node")

    def test_min(self):

        # Test for min in empty tree.
        got = self.tree.min()
        want = None
        self.assertEqual(got, want, "min failed on empty tree, should be None")

        # Test for min with only root node.
        self.tree.insert(0)
        got = self.tree.min()
        want = 0
        self.assertEqual(got.key, want, "min failed with only root node")

        # Test for min with all values less than root node.
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.min()
        want = -2
        self.assertEqual(got.key, want, "min failed with all values less than original root node")

        # Test for min with all values greater than root node.
        self.tree = rb.RedBlackTree()
        self.tree.insert(0)
        self.tree.insert(1)
        self.tree.insert(2)
        got = self.tree.min()
        want = 0
        self.assertEqual(got.key, want, "min failed with all values greater than original root node")

        # Test for min in tree with values less than and greater than root node.
        self.tree.insert(-1)
        self.tree.insert(-2)
        got = self.tree.min()
        want = -2
        self.assertEqual(got.key, want, "min failed with values greater and less than original root node")

    def test_left_rotation(self):

        # Test for left rotation by inserting two values greater than root node.
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

        # Test for right rotation by inserting two values less than root node.
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
        
        # Test that node is not root and node's parent is black.
        self.tree.insert(0)
        self.tree.insert(-1)
        got = self.tree.root.left
        self.assertEqual(self.tree.root, got.parent, "_rebalance has incorrect parent pointer")
        self.assertTrue(got, "_rebalance colored node black, should be red")

        # Test that node's parent is red and one of grandparent's 
        # left or right children is None.
        # See test_left_rotation and test_right_rotation.

        # Test that node's grandparents left and right children are red.
        # See test_case1.

        # Test that node's parent is red and the other child of the grandparent
        # of the node is black.
        # See test_left_rotation and test_right_rotation.

    def test_insert(self):

        # Test insert to an empty tree.
        self.tree.insert(0)
        want = rbn.Node(0)
        want.recolor()
        self.assertEqual(self.tree.root.key, want.key, "insert into empty tree failed, keys not equal")
        self.assertEqual(self.tree.root.instances, want.instances, "insert into empty tree failed, instances not equal")
        self.assertEqual(self.tree.root.parent, want.parent, "insert in to empty tree failed, parent pointers not equal")
        self.assertEqual(self.tree.root.left, want.left, "insert into empty tree failed, left child should be None")
        self.assertEqual(self.tree.root.right, want.right, "insert into empty tree failed, right child should be None")
        self.assertFalse(self.tree.root.is_red, "insert root into empty tree failed, root should be black not red")

        # Test insert value less than root.
        self.tree.insert(-1)
        self.assertEqual(self.tree.root.left.key, -1, "inserting a smaller element into the tree failed")
        self.assertEqual(self.tree.root.key, self.tree.root.left.parent.key, "left child's parent not correct")

        # Test insert value greater than root.
        self.tree.insert(1)
        self.assertEqual(self.tree.root.right.key, 1, "inserting a larger element into the tree failed")
        self.assertEqual(self.tree.root.key, self.tree.root.right.parent.key, "right child's parent not correct")

        # Test insert duplicate value.
        self.tree.insert(1)
        want = 2
        self.assertEqual(self.tree.root.right.instances, want, "inserting a duplicate value failed")

        # Test insert multiple values.
        self.tree = rb.RedBlackTree()
        self.tree.insert(10)
        self.tree.insert(0)
        self.tree.insert(20)
        self.tree.insert(-10)
        self.tree.insert(-9)
        self.tree.insert(-20)
        self.tree.insert(-30)
        self.tree.insert(19)
        self.tree.insert(30)
        self.tree.insert(18)

    def test_case1(self):

        # Test to ensure colors get changed, not worried about red-black.
        # maintenance
        self.tree.insert(0)
        self.tree.insert(-1)
        self.tree.insert(1)
        self.tree.insert(2)
        self.assertFalse(self.tree.root.is_red, "_case1 failure, root not black")
        self.assertFalse(self.tree.root.left.is_red, "_case1 failure, root's left child should be black")
        self.assertFalse(self.tree.root.right.is_red, "_case1 failure, root's right child should be black")
        self.assertTrue(self.tree.root.right.right.is_red, "_case1 failure last inserted node should be red")

    def test_case2(self):

        # Test to ensure rotations occur and colors are changed, not
        # worried about red-black maintenance.
        pass

    def test_traverse(self):

        # Test default with root node traversal.
        self.tree.insert(-10)
        got = self.tree.traverse(self.tree.root)
        want = [-10]
        self.assertEqual(got, want, "traverse of one element tree failed")

        # Test traversal of root and one left node.
        self.tree.insert(-20)
        got = self.tree.traverse(self.tree.root)
        want = [-20, -10]
        self.assertEqual(got, want, "traverse of tree with root greater than child failed")

        # Test traversal of root and one right node.
        self.tree = rb.RedBlackTree()
        self.tree.insert(-10)
        self.tree.insert(0)
        got = self.tree.traverse(self.tree.root)
        want = [-10, 0]
        self.assertEqual(got, want, "traverse of tree with child greater than root failed")

        # Test traversal of tree with root and two children.
        self.tree.insert(-20)
        got = self.tree.traverse(self.tree.root)
        want = [-20, -10, 0]
        self.assertEqual(got, want, "traverse of tree with two children failed")

        # Test traversal of tree with multiple nodes.
        self.tree.insert(-5)
        self.tree.insert(5)
        self.tree.insert(10)
        got = self.tree.traverse(self.tree.root)
        want = [-20, -10, -5, 0, 5, 10]
        self.assertEqual(got, want, "traverse of tree with multiple nodes failed")

        # Test traversal of tree with multiple instances of a node.
        self.tree.insert(0)
        got = self.tree.traverse(self.tree.root)
        want = [-20, -10, -5, 0, 5, 10]
        self.assertEqual(got, want, "traverse of tree with multiple nodes failed")

    def test_successor(self):

        # Test easy case.
        # Test other case.
        # Test key not in search tree.
        pass

    def test_predecessor(self):

        # Test easy case.
        # Test other case.
        # Test key not in search tree.
        pass

    def test_delete_instance(self):

        # Test no nodes in tree.
        got = self.tree.delete_instance(None)
        want = None
        self.assertEqual(got, want, "None value should be returned with no nodes in tree")

        # Test removing one instance.
        # self.tree.insert(0)
        # got = self.tree.delete_instance(0)
        # want = None
        # self.assertEqual(got, want, "None value should be returned when all instances of node deleted")

        # Test removing a second instance.
        # Test removing a node so the instances go to 0.

    def test_delete(self):

        # Test no nodes in tree.
        got = self.tree.delete(None)
        want = None
        self.assertEqual(got, want, "None value should be returned with no nodes in tree")

        # Test case 1 deletion: node is red with no children.
        self.tree.insert(0)
        # Insert the red node.
        self.tree.insert(1)
        self.tree.delete(1)
        self.assertEqual(self.tree.root.right, None, "red node not deleted")

        # Test case 2 deletion: node is black, node has only one child, 
        # and the child is red.
        # Delete the root with only one node.
        self.tree.insert(-1)
        self.tree.delete(0)
        want = -1
        self.assertEqual(self.tree.root.key, want, "root not deleted")
        self.assertFalse(self.tree.root.is_red, "new root not recolored after delete")
        self.assertEqual(self.tree.root.left, None, "left pointer not adjusted after delete")
        self.assertEqual(self.tree.root.right, None, "right pointer not adjusted after delete")

        # Delete a node that is not the root with only a red right child.
        self.tree.insert(-2)
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.delete(1)

        got = self.tree.root.right
        want = rbn.Node(2)
        want.recolor() # want is now red
        want.parent = self.tree.root
        self.assertEqual(got.key, want.key, "node not deleted properly")
        self.assertEqual(got.parent, want.parent, "node not given proper parent after delete ran")
        self.assertEqual(got.right, None, "got node should not have a child")
        self.assertEqual(got.left, None, "got node should not have a child")
        self.assertFalse(got.is_red, "node not correct color after deletion rebalancing")

        # Delete a node that is not the root with only a red left child.
        self.tree.insert(0)
        self.tree.delete(2)
        got = self.tree.root.right
        want = rbn.Node(0)
        want.recolor() # want is now red
        want.parent = self.tree.root
        self.assertEqual(got.key, want.key, "node not deleted properly")
        self.assertEqual(got.parent, want.parent, "node not given proper parent after delete ran")
        self.assertEqual(got.right, None, "got node should not have a child")
        self.assertEqual(got.left, None, "got node should not have a child")
        self.assertFalse(got.is_red, "node not correct color after deletion rebalancing")

        # Test case 3 deletion: node is black.
        # Test case 3.1: node's sibling is red.
        # self.tree = rb.RedBlackTree()
        # self.tree.insert(10)
        # self.tree.insert(0)
        # self.tree.insert(20)
        # self.tree.insert(-10)
        # self.tree.insert(-9)
        # self.tree.insert(-20)
        # self.tree.insert(-30)
        # self.assertTrue(self.tree.root.right.is_red)
        # self.assertFalse(self.tree.root.left.is_red)
        # Test case 3.2: node's sibling, s, is black and both children
        # of s are black.
        # Test case 3.3: node's sibling, s, is black and s's left child is red.
        # Test case 3.4: node's sibling, s, is black and s's right child is red. 
        

if __name__ == "__main__":
    unittest.main()