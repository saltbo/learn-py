# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if tree is None:
        return True

    return dfs(tree.left, tree.right)


def dfs(tree1, tree2):
    # If both trees are None, they are symmetric
    if tree1 is None and tree2 is None:
        return True

    # If one tree is None and the other is not, they are not symmetric
    if tree1 is None or tree2 is None:
        return False

    # Check if the current nodes are equal and recursively check the left and right subtrees
    # in opposite order to ensure symmetry
    # Compare the values of the current nodes
    # and check the left subtree of the first tree with the right subtree of the second tree
    # and the right subtree of the first tree with the left subtree of the second tree
    # If the values are not equal, the trees are not symmetric
    # If the values are equal, continue checking the subtrees
    return tree1.value == tree2.value and dfs(tree1.left, tree2.right) and dfs(tree1.right, tree2.left)
