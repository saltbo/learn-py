# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import splitBinaryTree as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = program.BinaryTree(2)
        tree.left = program.BinaryTree(4)
        tree.left.left = program.BinaryTree(4)
        tree.left.right = program.BinaryTree(6)
        tree.right = program.BinaryTree(10)
        tree.right.left = program.BinaryTree(3)
        tree.right.right = program.BinaryTree(3)
        expected = 16
        actual = program.splitBinaryTree(tree)
        self.assertEqual(actual, expected)
