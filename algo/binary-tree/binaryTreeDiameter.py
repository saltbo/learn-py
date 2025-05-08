# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def binaryTreeDiameter(tree):
#     currentMax = [0]
#     dfs(tree, currentMax)
#     return currentMax[0]


# def dfs(tree, currentMax):
#     if not tree:
#         return 0

#     leftDepth = dfs(tree.left, currentMax)
#     rightDepth = dfs(tree.right, currentMax)
#     currentMax[0] = max(currentMax[0], leftDepth+rightDepth)

#     return max(leftDepth, rightDepth) + 1

def binaryTreeDiameter(tree):
    global currentMax
    currentMax = 0
    dfs(tree)
    return currentMax


def dfs(tree):
    global currentMax
    if tree is None:
        return 0

    left = dfs(tree.left)
    right = dfs(tree.right)
    currentMax = max(currentMax, left+right)

    return max(left, right)+1
