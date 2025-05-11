# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import heightBalancedBinaryTree as program
import unittest

BinaryTree = program.BinaryTree


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        expected = True
        actual = program.heightBalancedBinaryTree(root)
        self.assertEqual(actual, expected)
