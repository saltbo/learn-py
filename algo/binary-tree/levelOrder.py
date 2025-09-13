from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    queue = deque([root])
    while queue:
        level_vals = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr is None:
                break

            level_vals.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(level_vals)
    return res
