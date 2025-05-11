# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor1(tree, node):
    array = []
    dfs(tree, array)
    for idx, item in enumerate(array):
        if idx == len(array)-1:
            break
        if item == node:
            return array[idx+1]

    return None


def dfs(tree, array):
    if tree is None:
        return

    dfs(tree.left, array)
    array.append(tree)
    dfs(tree.right, array)


def findSuccessor2(tree, node):
    if node.right is not None:
        current = node.right
        while current.left:
            current = current.left
        return current

    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent


def findSuccessor(tree, node):
    global return_next, successor
    return_next, successor = False, None
    dfs3(tree, node)
    return successor


def dfs3(tree, node):
    if tree is None:
        return

    dfs3(tree.left, node)
    global return_next, successor
    if return_next:
        successor = tree
        return_next = False
        return
    if tree is node:
        return_next = True
    dfs3(tree.right, node)
