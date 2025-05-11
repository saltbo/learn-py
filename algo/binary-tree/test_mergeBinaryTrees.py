# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import mergeBinaryTrees as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = program.BinaryTree(1)
        tree1.left = program.BinaryTree(3)
        tree1.left.left = program.BinaryTree(7)
        tree1.left.right = program.BinaryTree(4)
        tree1.right = program.BinaryTree(2)

        tree2 = program.BinaryTree(1)
        tree2.left = program.BinaryTree(5)
        tree2.left.left = program.BinaryTree(2)
        tree2.right = program.BinaryTree(9)
        tree2.right.left = program.BinaryTree(7)
        tree2.right.right = program.BinaryTree(6)

        actual = program.mergeBinaryTrees(tree1, tree2)
        self.assertEqual(actual.value, 2)
        self.assertEqual(actual.left.value, 8)
        self.assertEqual(actual.left.left.value, 9)
        self.assertEqual(actual.left.right.value, 4)
        self.assertEqual(actual.right.value, 11)
        self.assertEqual(actual.right.left.value, 7)
        self.assertEqual(actual.right.right.value, 6)
