from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []
    queue = deque([root])
    should_reverse = False
    while (queue):
        level_vals = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            level_vals.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if should_reverse:
            level_vals.reverse()

        res.append(level_vals)
        should_reverse = not should_reverse
    return res
