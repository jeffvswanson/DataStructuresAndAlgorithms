# test_search_tree_node.py

import unittest

import search_tree_node as n

class TestSearchTreeNode(unittest.TestCase):

    def setUp(self):
        self.node = n.Node(1)
        
    def test_recolor(self):
        self.node.recolor()
        self.assertEqual(self.node.color, "black", "wrong color after recolor")

    def test_set_key(self):
        self.node.set_key(0)
        want = 0
        self.assertEqual(self.node.key, want, "key value not changed with set")

    def test_add_instance(self):
        self.node.add_instance()
        want = 2
        self.assertEqual(self.node.instances, want, "number of node occurrences not updated")

if __name__ == "__main__":
    unittest.main()