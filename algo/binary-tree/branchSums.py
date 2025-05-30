from tomlkit import value


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def branchSums(root):
    # Write your code here.
    sums = []
    dfs(root, 0, sums)
    return sums


def dfs(node, valueSum, sums):
    if node is None:
        return 

    valueSum += node.value
    if node.left is None and node.right is None:
        sums.append(valueSum)
        return

    dfs(node.left, valueSum, sums)
    dfs(node.right, valueSum, sums)




tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
print(branchSums(tree))