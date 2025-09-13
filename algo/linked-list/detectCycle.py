from typing import Optional
from helper2 import ListNode, create_cycle_linked_list


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# 运行测试
"""测试detectCycle函数"""
print("=== detectCycle 测试 ===")

# 测试1: [3,2,0,-4], pos=1
print("测试1: [3,2,0,-4], pos=1")
node1 = create_cycle_linked_list([3, 2, 0, -4], 1)
result1 = detectCycle(node1)
print(f"返回环入口节点值: {result1.val if result1 else None}")

# 测试2: [1,2], pos=0
print("\n测试2: [1,2], pos=0")
node2 = create_cycle_linked_list([1, 2], 0)
result2 = detectCycle(node2)
print(f"返回环入口节点值: {result2.val if result2 else None}")

# 测试3: [1], 无环
print("\n测试3: [1], 无环")
node3 = create_cycle_linked_list([1], -1)
result3 = detectCycle(node3)
print(f"返回: {result3}")

print("=== 测试结束 ===")
