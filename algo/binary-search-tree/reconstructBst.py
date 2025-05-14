# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return

    currentValue = preOrderTraversalValues[0]
    rightIdx = len(preOrderTraversalValues)
    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightIdx = idx
            break

    left = reconstructBst(preOrderTraversalValues[1:rightIdx])
    right = reconstructBst(preOrderTraversalValues[rightIdx:])
    bst = BST(currentValue, left, right)
    return bst


values = [10, 4, 2, 1, 5, 17, 19, 18]
reconstructBst(values)
