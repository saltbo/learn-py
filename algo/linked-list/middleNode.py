# This is an input class. Do not edit.
from helper import create_linked_list, print_linked_list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    singleStepNode = linkedList
    doubleStepNode = linkedList
    count = 0
    while (doubleStepNode is not None and doubleStepNode.next is not None):
        singleStepNode = singleStepNode.next
        doubleStepNode = doubleStepNode.next.next
        count += 1

    return singleStepNode


def middleNode2(linkedList):
    count = 0
    currentNode = linkedList
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middleNode = linkedList
    for _ in range(count//2):
        middleNode = middleNode.next

    return middleNode


data = {
    "linkedList": {
        "head": "1",
        "nodes": [
            {"id": "1", "next": "2", "value": 1},
            {"id": "2", "next": "3", "value": 2},
            {"id": "3", "next": None, "value": 3}
        ]
    }
}


head = create_linked_list(data['linkedList'])
print_linked_list(head)
print_linked_list(middleNode(head))
print_linked_list(middleNode2(head))

print(5//2)