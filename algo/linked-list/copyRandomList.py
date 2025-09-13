from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    m = {}
    curr = head
    while curr:
        m[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        if curr.next:
            m[curr].next = m[curr.next]
        if curr.random:
            m[curr.random] = m[curr.random]
        curr = curr.next

    return m[head]


def create_linked_list_with_random_pointers(arr):
    if not arr:
        return None

    nodes = [Node(x) for x, _ in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, (_, random_index) in enumerate(arr):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


if __name__ == "__main__":
    arr = [(7, 2), (13, None), (11, 0), (10, 2)]
    head = create_linked_list_with_random_pointers(arr)
    copyRandomList(head)
