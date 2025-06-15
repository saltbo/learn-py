# This is an input class. Do not edit.
from operator import is_


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def invertedBisection(head):
    if head is None or head.next is None:
        return head
    debug_print(head)

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow
    print(middle.value)
    linkedListLen = calc_length(head)
    is_odd = linkedListLen % 2 != 0

    debug_print(head)
    left, right = split_linked_list(head, middle, is_odd)
    debug_print(left)
    debug_print(right)
    reversed_part1 = reverse_linked_list(left)
    reversed_part2 = reverse_linked_list(right)
    debug_print(reversed_part1)
    debug_print(reversed_part2)
    return merge(reversed_part1, reversed_part2,
                 is_odd, middle)


def merge(part1, part2, odd, middle):
    node = part1
    while node:
        if node.next == None:
            break
        node = node.next
    if not odd:
        node.next = part2
    else:
        middle.next = part2
        node.next = middle
    return part1


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        raw_next = current.next
        current.next = prev
        prev = current
        current = raw_next

    return prev


def split_linked_list(head, middle, odd):
    node = head
    right = None
    prev = None
    while node:
        if node.value == middle.value:
            right = node.next if odd else node
            prev.next = None
            break

        prev = node
        node = node.next
    return (head, right)


def calc_length(head):
    node = head
    count = 0
    while node:
        count += 1
        node = node.next
    return count


def debug_print(head):
    node = head
    items = []
    while node is not None:
        items.append(str(node.value))
        node = node.next

    print("->".join(items))
