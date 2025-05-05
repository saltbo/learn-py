# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    count = 1
    sNode = head
    eNode = head
    while (count <= k):
        eNode = eNode.next
        count += 1

    if eNode is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while (eNode.next is not None):
        eNode = eNode.next
        sNode = sNode.next

    sNode.next = sNode.next.next
