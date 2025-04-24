def nodeDepths(root):
    # Write your code here.
    return dfs(root, 0)


def dfs(node, depth):
    if node is None:
        return 0

    return depth + dfs(node.left, depth+1) + dfs(node.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
