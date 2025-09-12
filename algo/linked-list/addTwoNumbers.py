from typing import Optional
from helper2 import ListNode, create_linked_list, print_linked_list


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    node1 = l1
    node2 = l2

    head = ListNode()
    current = head
    carry = 0
    while node1 or node2 or carry:
        val1 = node1.val if node1 else 0
        val2 = node2.val if node2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    return head.next


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print_linked_list(result)  # 输出: 7 -> 0 -> 8
