# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height


def heightBalancedBinaryTree(tree):
    return dfs(tree).balanced


def dfs(tree) -> TreeInfo:
    if tree is None:
        return TreeInfo(True, -1)

    left = dfs(tree.left)
    right = dfs(tree.right)

    balanced = (
        left.balanced and right.balanced
        and abs(left.height - right.height) <= 1
    )
    height = max(left.height, right.height)+1
    return TreeInfo(balanced, height)
