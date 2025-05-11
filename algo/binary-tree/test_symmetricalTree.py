# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import symmetricalTree as program
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(10)
        tree.left = BinaryTree(5)
        tree.right = BinaryTree(5)
        tree.left.left = BinaryTree(7)
        tree.left.right = BinaryTree(9)
        tree.right.left = BinaryTree(9)
        tree.right.right = BinaryTree(7)
        expected = True
        actual = program.symmetricalTree(tree)
        self.assertEqual(actual, expected)
