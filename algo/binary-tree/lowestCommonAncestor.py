class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node: TreeNode):
        if not node or node is p or node is q:
            return node

        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            return node

        return left if left else right

    return dfs(root)
