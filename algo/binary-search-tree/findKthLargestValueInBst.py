# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    values = []
    inOrderTraverse(tree, values)
    return values[len(values)-k]


def inOrderTraverse(tree, values):
    if tree is None:
        return

    inOrderTraverse(tree.left, values)
    values.append(tree.value)
    inOrderTraverse(tree.right, values)
