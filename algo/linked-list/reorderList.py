
from typing import Optional
from helper2 import ListNode, create_linked_list, print_linked_list


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    stack = []
    node = head
    while node:
        stack.append(node)
        node = node.next

    left = 0
    right = len(stack) - 1
    while left < right:
        stack[left].next = stack[right]
        left += 1

        if left >= right:
            break

        stack[right].next = stack[left]
        right -= 1

    stack[left].next = None


node1 = create_linked_list([1, 2, 3, 4])
node2 = create_linked_list([1, 2, 3, 4, 5])
reorderList(node1)
print_linked_list(node1)
reorderList(node2)
print_linked_list(node2)
