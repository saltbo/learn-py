# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            # for the empty LinkedList
            self.head = node
            self.tail = node
            return

        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            # for the empty LinkedList
            self.setHead(node)
            return

        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is not None:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert

        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return

        node = self.head
        currentPosition = 0
        while (node != None):
            currentPosition += 1
            if currentPosition == position:
                self.insertBefore(node, nodeToInsert)
                break
            node = node.next

    def removeNodesWithValue(self, value):
        node = self.head
        while (node != None):
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        node = self.head
        while (node != None):
            if node.value == value:
                return True
            node = node.next
        return False
