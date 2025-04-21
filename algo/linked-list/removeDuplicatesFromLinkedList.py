from helper import create_linked_list, print_linked_list


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        if nextNode is not None and currentNode.value == nextNode.value:
            currentNode.next = nextNode.next
            continue
        currentNode = currentNode.next

    return linkedList


data = {
    "linkedList": {
        "head": "1",
        "nodes": [
            {"id": "1", "next": "1-2", "value": 1},
            {"id": "1-2", "next": "1-3", "value": 1},
            {"id": "1-3", "next": "2", "value": 1},
            {"id": "2", "next": "3", "value": 3},
            {"id": "3", "next": "3-2", "value": 4},
            {"id": "3-2", "next": "3-3", "value": 4},
            {"id": "3-3", "next": "4", "value": 4},
            {"id": "4", "next": "5", "value": 5},
            {"id": "5", "next": "5-2", "value": 6},
            {"id": "5-2", "next": None, "value": 6}
        ]
    }
}


head = create_linked_list(data['linkedList'])
print_linked_list(head)
print_linked_list(removeDuplicatesFromLinkedList(head))
