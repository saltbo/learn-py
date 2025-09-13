from typing import Optional
from helper2 import ListNode, create_linked_list, print_linked_list


node = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(node)

# Reverse
prev = None
curr = node

while curr:
    nn = curr.next  # save the next node
    curr.next = prev  # reverse to the prev node
    prev = curr  # prepare the next loop prev
    curr = nn  # point to the next node
print_linked_list(prev)
print("--------------")


# Find the middle node
def find_middle_node(node):
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


node1 = create_linked_list([1, 2, 3, 4])
node2 = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(find_middle_node(node1))
print_linked_list(find_middle_node(node2))
print("--------------")


# Detect whether a cycle
def has_cycle(node):
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


node3 = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(node3)
print(has_cycle(node3))

# link the tail to the head
curr = node3
while curr:
    if curr.next is None:
        curr.next = node3
        break
    curr = curr.next

print(has_cycle(node3))

print("--------------")
node4 = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(node4)
target = 3

# remove the specify node
dummy = ListNode(0)
dummy.next = node4
curr = dummy
while curr.next:
    if curr.next.val == target:
        curr.next = curr.next.next
    curr = curr.next

print_linked_list(dummy.next)
