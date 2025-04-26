def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest

    if abs(closest-target) > abs(tree.value-target):
        closest = tree.value

    if target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    elif target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    else:
        return closest


def findClosestValueInBstByIterate(tree, target):
    currentNode = tree
    closest = currentNode.value
    while (currentNode is not None):
        if abs(closest-target) > abs(currentNode.value-target):
            closest = currentNode.value

        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break

    return closest


# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
