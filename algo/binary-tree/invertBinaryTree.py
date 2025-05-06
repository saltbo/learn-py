def invertBinaryTree(tree):
    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def invertBinaryTree2(tree):
    queue = [tree]
    while len(queue) > 0:
        current = queue.pop()
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)


def swap(node):
    node.left, node.right = node.right, node.left

# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
