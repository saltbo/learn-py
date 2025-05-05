# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    numOne = linkedListOne
    numTwo = linkedListTwo

    carry = 0
    newLinkedList = LinkedList(0)
    currentNode = newLinkedList
    while numOne is not None or numTwo is not None or carry != 0:
        sum = carry
        if numOne is not None:
            sum += numOne.value
        if numTwo is not None:
            sum += numTwo.value
        carry = sum//10
        print(sum, carry)

        newNode = LinkedList(sum % 10)
        currentNode.next = newNode
        currentNode = currentNode.next

        numOne = numOne.next if numOne is not None else None
        numTwo = numTwo.next if numTwo is not None else None
    return newLinkedList.next
