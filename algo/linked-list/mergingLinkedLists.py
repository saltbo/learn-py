# This is an input class. Do not edit.
import copy


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    listOneNode = linkedListOne
    listOneLength = 0
    while listOneNode is not None:
        listOneLength += 1
        listOneNode = listOneNode.next

    listTwoNode = linkedListTwo
    listTwoLength = 0
    while (listTwoNode is not None):
        listTwoLength += 1
        listTwoNode = listTwoNode.next

    # If the two lists are the different length, we need to move the pointer of the longer list first
    if listOneLength > listTwoLength:
        longerOne = linkedListOne
        shorterOne = linkedListTwo
    else:
        longerOne = linkedListTwo
        shorterOne = linkedListOne
    # We can also use the following code to determine which one is longer but it's not eazy to read
    # longerOne = linkedListOne if listOneLength > listTwoLength else linkedListTwo
    # shorterOne = linkedListTwo if listOneLength > listTwoLength else linkedListOne
    for _ in range(abs(listOneLength-listTwoLength)):
        longerOne = longerOne.next

    # Now we can move both pointers at the same time
    return findIntersectionNode(longerOne, shorterOne)


def findIntersectionNode(nodeOne, nodeTwo):
    currentOneNode = nodeOne
    currentTwoNode = nodeTwo
    while currentOneNode is not None:
        if currentOneNode == currentTwoNode:
            return currentOneNode

        currentOneNode = currentOneNode.next
        currentTwoNode = currentTwoNode.next

    return None


def mergingLinkedLists2(linkedListOne, linkedListTwo):
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    # When the first pointer reaches the end of the first list, we move it to the head of the second list
    # When the second pointer reaches the end of the second list, we move it to the head of the first list
    # This way, both pointers will traverse the same number of nodes
    # in the end, and they will meet at the intersection node
    # If there is no intersection, both pointers will be None
    while nodeOne != nodeTwo:
        nodeOne = linkedListTwo if nodeOne is None else nodeOne.next
        nodeTwo = linkedListOne if nodeTwo is None else nodeTwo.next

    return nodeOne
