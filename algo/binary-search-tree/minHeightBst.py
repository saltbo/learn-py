def minHeightBst(array):
    return construct(array, None, 0, len(array)-1)


def construct(array, bst, start, end):
    if end < start:
        return

    midIdx = (start+end)//2
    midValue = array[midIdx]
    if bst is None:
        bst = BST(midValue)
    else:
        bst.insert(midValue)

    construct(array, bst, start, midIdx-1)
    construct(array, bst, midIdx+1, end)
    return bst


def construct2(array, start, end):
    if end < start:
        return
    midIdx = (start+end)//2
    bst = BST(array[midIdx])
    bst.left = construct2(array, start, midIdx-1)
    bst.right = construct2(array, midIdx+1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def height(self):
        if self is None:
            return 0
        leftHeight = self.left.height() if self.left else 0
        rightHeight = self.right.height() if self.right else 0
        return max(leftHeight, rightHeight) + 1


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
print(minHeightBst(array).height())
