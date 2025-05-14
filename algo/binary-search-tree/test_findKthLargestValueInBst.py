# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import findKthLargestValueInBst as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BST(15)
        root.left = program.BST(5)
        root.left.left = program.BST(2)
        root.left.left.left = program.BST(1)
        root.left.left.right = program.BST(3)
        root.left.right = program.BST(5)
        root.right = program.BST(20)
        root.right.left = program.BST(17)
        root.right.right = program.BST(22)
        k = 3
        expected = 17
        actual = program.findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)
