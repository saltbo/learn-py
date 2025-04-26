# This is an input class. Do not edit.
from math import floor


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.

    return dfs(tree)


def dfs(node):
    if node.left is None and node.right is None:
        return node.value

    operatorNum = node.value
    if operatorNum == -1:
        return dfs(node.left)+dfs(node.right)
    elif operatorNum == -2:
        return dfs(node.left)-dfs(node.right)
    elif operatorNum == -3:
        return dfs(node.left)//dfs(node.right)
    elif operatorNum == -4:
        return dfs(node.left)*dfs(node.right)
    return -1

root = BinaryTree(1)
evaluateExpressionTree(root)


print(9/-2)
print(9//-2)
print(int(9/-2))

print(floor(1.9))
print(floor(-1.1))