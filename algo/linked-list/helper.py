class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


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
