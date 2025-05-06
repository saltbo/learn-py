# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import mergingLinkedLists as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        l1 = program.LinkedList(1)
        l1.next = program.LinkedList(2)
        l2 = program.LinkedList(3)
        l2.next = l1.next

        expected = l1.next
        actual = program.mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)
