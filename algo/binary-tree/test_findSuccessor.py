# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import findSuccessor as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        root.left.parent = root
        root.right = program.BinaryTree(3)
        root.right.parent = root
        root.left.left = program.BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = program.BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = program.BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = program.findSuccessor(root, node)
        self.assertEqual(actual, expected)
