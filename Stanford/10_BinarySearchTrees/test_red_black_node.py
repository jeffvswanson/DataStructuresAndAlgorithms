# test_red_black_node.py

import unittest

import red_black_node as n

class TestSearchTreeNode(unittest.TestCase):

    def setUp(self):
        self.node = n.Node(1)
        
    def test_is_red(self):
        self.assertTrue(self.node.is_red, "wrong color on initialization")
        self.node.recolor()
        self.assertFalse(self.node.is_red, "wrong color after recolor from red, should be black")
        self.node.recolor()
        self.assertTrue(self.node.is_red, "wrong color after recoloring from black, should be red")

    def test_set_key(self):
        self.node.set_key(0)
        want = 0
        self.assertEqual(self.node.key, want, "key value not changed with set")

    def test_add_instance(self):
        self.node.add_instance()
        want = 2
        self.assertEqual(self.node.instances, want, "number of node occurrences not updated")

    def test_remove_instance(self):
        self.node.add_instance()
        self.node.add_instance()
        self.node.remove_instance()
        want = 2
        self.assertEqual(self.node.instances, want, "number of node occurrences not updated")

if __name__ == "__main__":
    unittest.main()