# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import binaryTreeDiameter as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(3)
        root.left.left = program.BinaryTree(7)
        root.left.left.left = program.BinaryTree(8)
        root.left.left.left.left = program.BinaryTree(9)
        root.left.right = program.BinaryTree(4)
        root.left.right.right = program.BinaryTree(5)
        root.left.right.right.right = program.BinaryTree(6)
        root.right = program.BinaryTree(2)
        expected = 6
        actual = program.binaryTreeDiameter(root)
        self.assertEqual(actual, expected)
