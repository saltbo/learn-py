

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTreeByInOrder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not preorder:
        return None

    inorder_indexes = {v: i for i, v in enumerate(inorder)}

    curr_pre_idx = 0

    def buildSubTree(left, right):
        if left > right:
            return None

        nonlocal curr_pre_idx
        root_val = preorder[curr_pre_idx]
        curr_pre_idx += 1

        mid = inorder_indexes[root_val]
        root = root = TreeNode(root_val)
        root.left = buildSubTree(left, mid - 1)
        root.right = buildSubTree(mid + 1, right)
        return root

    return buildSubTree(0, len(inorder) - 1)


def buildTreeByPostOrder(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not postorder:
        return None

    inorder_indexes = {v: i for i, v in enumerate(inorder)}

    curr_post_idx = len(postorder) - 1

    def build_subtree(left, right):
        if left > right:
            return None

        nonlocal curr_post_idx

        root_val = postorder[curr_post_idx]
        curr_post_idx -= 1

        mid = inorder_indexes[root_val]
        root = TreeNode(root_val)
        root.right = build_subtree(mid + 1, right)
        root.left = build_subtree(left, mid - 1)
        return root

    return build_subtree(0, len(inorder) - 1)


def inorder_traverse(node: Optional[TreeNode]) -> List[int]:
    return [] if not node else inorder_traverse(node.left) + [node.val] + inorder_traverse(node.right)


def preorder_traverse(node: Optional[TreeNode]) -> List[int]:
    return [] if not node else [node.val] + preorder_traverse(node.left) + preorder_traverse(node.right)


def postorder_traverse(node: Optional[TreeNode]) -> List[int]:
    return [] if not node else postorder_traverse(node.left) + postorder_traverse(node.right) + [node.val]


if __name__ == "__main__":
    # preorder
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = buildTreeByInOrder(pre, ino)
    print("Reconstructed preorder:", preorder_traverse(root))
    print("Reconstructed inorder :", inorder_traverse(root))

    # postorder
    post = [9, 15, 7, 20, 3]
    ino = [9, 3, 15, 20, 7]
    root = buildTreeByPostOrder(ino, post)
    print("Reconstructed postorder:", postorder_traverse(root))
    print("Reconstructed inorder  :", inorder_traverse(root))
