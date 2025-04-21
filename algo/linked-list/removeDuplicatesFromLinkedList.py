class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        if nextNode is not None and currentNode.value == nextNode.value:
            currentNode.next = nextNode.next
            continue
        currentNode = currentNode.next

    return linkedList


ll = {
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

# Create linked list from the given data structure


def create_linked_list(data):
    nodes = {}
    for node_data in data['nodes']:
        node_id = node_data['id']
        value = node_data['value']
        nodes[node_id] = LinkedList(value)

    for node_data in data['nodes']:
        node_id = node_data['id']
        next_node_id = node_data['next']
        if next_node_id:
            nodes[node_id].next = nodes[next_node_id]

    return nodes[data['head']]

# Print the linked list to verify its structure


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")


head = create_linked_list(ll['linkedList'])
print_linked_list(head)
print_linked_list(removeDuplicatesFromLinkedList(head))
