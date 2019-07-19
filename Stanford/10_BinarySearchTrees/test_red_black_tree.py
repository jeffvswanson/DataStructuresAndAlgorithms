# test_red_black_tree.py

import unittest

import red_black_tree as rb

class TestRedBlackBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = rb.RedBlackTree()

    def test_contains(self):

        search_value = 0
        # Test for match
        self.tree.root.set_key(0)
        got = self.tree.contains(search_value, self.tree.root)
        want = (0, True)
        self.assertTupleEqual(got, want)

        # Test for value less than comparison node, also tests no match
        self.tree.root.set_key(1)
        got = self.tree.contains(search_value, self.tree.root)
        want = (None, False)
        self.assertEqual(got, want)

        # Test for value greater than comparison node
        self.tree.root.set_key(-1)
        got = self.tree.contains(search_value, self.tree.root)
        want = (None, False)
        self.assertTupleEqual(got, want)

if __name__ == "__main__":
    unittest.main()