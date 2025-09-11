from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def create_linked_list(arr):
    """辅助函数：将数组转换为链表"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    """辅助函数：打印链表"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result)


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(print_linked_list(result))  # 输出: 7 -> 0 -> 8
