# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree1(tree):
    halfOfSum = sumOfTree(tree)/2
    return halfOfSum if treeSubTrees(tree, halfOfSum)[1] else 0


def treeSubTrees(tree, halfOfSum):
    if tree is None:
        return (0, False)

    leftSum, leftCanBeSplit = treeSubTrees(tree.left, halfOfSum)
    rightSum, rightCanBeSplit = treeSubTrees(tree.right, halfOfSum)
    currentSum = tree.value + leftSum + rightSum
    return (currentSum, leftCanBeSplit or rightCanBeSplit or currentSum == halfOfSum)


def splitBinaryTree(tree):
    halfOfSum = sumOfTree(tree)/2
    return halfOfSum if canBeSplit(tree, halfOfSum) else 0


def canBeSplit(tree, target):
    if tree is None:
        return False

    if sumOfTree(tree) == target:
        return True

    return canBeSplit(tree.left, target) or canBeSplit(tree.right, target)


def sumOfTree(tree):
    if tree is None:
        return 0

    return tree.value + sumOfTree(tree.left)+sumOfTree(tree.right)
