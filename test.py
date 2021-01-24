import unittest
from AVLTree import AVLTree


class AvlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        cls.data20 = 20
        cls.data35 = 35
        cls.data40 = 40
        cls.data10 = 10

        cls.data50 = 50
        cls.data45 = 45
        cls.data30 = 30

        cls.dataD = "D"
        cls.dataB = "B"
        cls.dataC = "C"

        cls.d1 = 15
        cls.d2 = 20
        cls.d3 = 24
        cls.d4 = 10
        cls.d5 = 13
        cls.d6 = 7
        cls.d7 = 30
        cls.d8 = 36
        cls.d9 = 25

        cls.bbt1 = AVLTree()
        cls.bbt2 = AVLTree()
        cls.bbt3 = AVLTree()
        cls.bbt4 = AVLTree()

    def traverse_and_get_node(self, data, node):
        if node.left_node:
            _node = self.traverse_and_get_node(data, node.left_node)
            if _node:
                return _node
        if data == node.data:
            return node
        if node.right_node:
            return self.traverse_and_get_node(data, node.right_node)

    def setUp(self):
        # BBT AVL Tree 1
        self.bbt1.insert(self.data20)
        self.bbt1.insert(self.data35)
        self.bbt1.insert(self.data40)
        self.bbt1.insert(self.data10)

        # Test the root node data
        self.assertEqual(self.data35, self.bbt1.root.data)

        self.node_10 = self.traverse_and_get_node(10, self.bbt1.root)
        self.node_20 = self.traverse_and_get_node(self.data20, self.bbt1.root)
        self.node_35 = self.traverse_and_get_node(self.data35, self.bbt1.root)
        self.node_40 = self.traverse_and_get_node(self.data40, self.bbt1.root)

        # BBT AVL Tree 2
        self.bbt2.insert(self.data50)
        self.bbt2.insert(self.data45)
        self.bbt2.insert(self.data30)

        # Test the root node data
        self.assertEqual(self.data45, self.bbt2.root.data)

        self.node_50 = self.traverse_and_get_node(self.data50, self.bbt2.root)
        self.node_45 = self.traverse_and_get_node(self.data45, self.bbt2.root)
        self.node_30 = self.traverse_and_get_node(self.data30, self.bbt2.root)

        # BBT AVL Tree 3
        # Tree not doubly left heavy
        self.bbt3.insert(self.dataD)
        self.bbt3.insert(self.dataB)
        self.bbt3.insert(self.dataC)

        # Test the root node data
        self.assertEqual(self.dataC, self.bbt3.root.data)

        self.node_D = self.traverse_and_get_node(self.dataD, self.bbt3.root)
        self.node_B = self.traverse_and_get_node(self.dataB, self.bbt3.root)
        self.node_C = self.traverse_and_get_node(self.dataC, self.bbt3.root)

        # BBT AVL Tree 4
        self.bbt4.insert(self.d1)
        self.bbt4.insert(self.d2)
        self.bbt4.insert(self.d3)
        self.bbt4.insert(self.d4)
        self.bbt4.insert(self.d5)
        self.bbt4.insert(self.d6)
        self.bbt4.insert(self.d7)
        self.bbt4.insert(self.d8)
        self.bbt4.insert(self.d9)

    def test_traverse_and_get_node(self):
        print("test_traverse_and_get_node")
        self.assertEqual(self.data20, self.node_20.data)
        self.assertEqual(self.data35, self.node_35.data)
        self.assertEqual(self.data40, self.node_40.data)

    def test_left_right_height(self):
        print("test_left_right_height")
        left_height, right_height = self.bbt1.left_right_height(self.node_10)
        self.assertTupleEqual((left_height, right_height), (-1, -1))
        left_height, right_height = self.bbt1.left_right_height(self.node_20)
        self.assertTupleEqual((left_height, right_height), (0, -1))
        left_height, right_height = self.bbt1.left_right_height(self.node_35)
        self.assertTupleEqual((left_height, right_height), (1, 0))
        left_height, right_height = self.bbt1.left_right_height(self.node_40)
        self.assertTupleEqual((left_height, right_height), (-1, -1))

        self.assertEqual(self.node_35.height, 2)

    def test_check_balanced(self):
        print("test_check_balanced")

        self.assertEqual(self.bbt1.root.data, 35)

        # For Balanced Binary Tree 1
        self.assertEqual(None, self.node_10.left_node)
        self.assertEqual(None, self.node_10.right_node)

        # For Balanced Binary Tree 4
        self.assertEqual(self.bbt4.root.data, 13)
        left_node = self.traverse_and_get_node(10, self.bbt4.root)
        self.assertEqual(self.bbt4.root.left_node, left_node)
        right_node = self.traverse_and_get_node(24, self.bbt4.root)
        self.assertEqual(self.bbt4.root.right_node, right_node)

        self.assertEqual(7, left_node.left_node.data)
        self.assertEqual(30, right_node.right_node.data)
        self.assertEqual(25, right_node.right_node.left_node.data)

    def test_rotate_left(self):
        print("test_rotate_left")

        get_root = self.bbt1.root
        self.assertEqual(self.data35, get_root.data)
        self.assertEqual(get_root.left_node.data, 20)
        self.assertEqual(get_root.right_node.data, 40)
        self.assertEqual(self.node_20.parent.data, get_root.data)
        self.assertEqual(self.node_40.parent.data, get_root.data)

    def test_rotate_right(self):
        print("test_rotate_right")

        get_root = self.bbt2.root
        self.assertEqual(self.data45, get_root.data)
        self.assertEqual(get_root.left_node.data, 30)
        self.assertEqual(get_root.right_node.data, 50)
        self.assertEqual(self.node_30.parent.data, get_root.data)
        self.assertEqual(self.node_50.parent.data, get_root.data)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == "__main__":
    unittest.main()
