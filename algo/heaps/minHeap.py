# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        for currentIdx in range(self.parentIdx(len(array)-1), -1, -1):
            self.siftDown(currentIdx)

        return self.heap

    def siftDown(self, currentIdx):
        """
        Adjust the element at the given index downward to ensure the subtree satisfies the min heap property
        i.e., parent node value is less than or equal to its child node values
        """
        # Continue looping while the current node has at least one child
        while self.hasLeftChild(currentIdx):
            # Assume the left child is the smaller child
            smallerChildIdx = self.leftChildIdx(currentIdx)

            # If the right child exists and is smaller than the left child, update the smaller child to the right child
            if (self.hasRightChild(currentIdx) and
                    self.heap[self.rightChildIdx(currentIdx)] < self.heap[smallerChildIdx]):
                smallerChildIdx = self.rightChildIdx(currentIdx)

            # If the current node is already less than or equal to the smallest child, heap property is satisfied, exit loop
            if self.heap[currentIdx] <= self.heap[smallerChildIdx]:
                break

            # Otherwise swap the current node with the smaller child, and continue adjusting downward
            self.swap(currentIdx, smallerChildIdx)
            currentIdx = smallerChildIdx

    def siftUp(self, currentIdx):
        while currentIdx > 0 and self.heap[currentIdx] < self.heap[self.parentIdx(currentIdx)]:
            self.swap(currentIdx, self.parentIdx(currentIdx))
            currentIdx = self.parentIdx(currentIdx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1)
        val = self.heap.pop()
        self.siftDown(0)
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def swap(self, currentIdx, targetIdx):
        self.heap[currentIdx], self.heap[targetIdx] = self.heap[targetIdx], self.heap[currentIdx]

    def leftChildIdx(self, idx):
        return 2*idx+1

    def rightChildIdx(self, idx):
        return 2*idx+2

    def parentIdx(self, idx):
        return (idx-1)//2

    def hasLeftChild(self, idx):
        return self.leftChildIdx(idx) < len(self.heap)

    def hasRightChild(self, idx):
        return self.rightChildIdx(idx) < len(self.heap)
