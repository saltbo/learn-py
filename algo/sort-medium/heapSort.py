def heapSort(array):
    buildMaxHeap(array)
    for endIdx in range(len(array)-1, 0, -1):
        print(f"endIdx: {endIdx}")
        swap(array, 0, endIdx)
        siftDown(array, 0, endIdx-1)
    return array


def buildMaxHeap(array):
    firstParentIdx = (len(array)-2)//2
    for currentIdx in reversed(range(firstParentIdx+1)):
        siftDown(array, currentIdx, len(array)-1)


def siftDown(heap, currentIdx, endIdx):
    # This function ensures that the subtree rooted at currentIdx is a max-heap.
    while currentIdx*2+1 <= endIdx:
        leftChildIdx = currentIdx*2+1
        rightChildIdx = leftChildIdx+1
        largestOneIdx = leftChildIdx
        if rightChildIdx <= endIdx and heap[rightChildIdx] > heap[largestOneIdx]:
            largestOneIdx = rightChildIdx

        if heap[largestOneIdx] < heap[currentIdx]:
            break

        swap(heap, currentIdx, largestOneIdx)
        currentIdx = largestOneIdx


def siftDown2(heap, currentIdx, endIdx):
    leftChildIdx = currentIdx*2+1
    rightChildIdx = leftChildIdx+1

    if leftChildIdx > endIdx:
        return

    largestIdx = leftChildIdx
    if rightChildIdx <= endIdx and heap[rightChildIdx] > heap[leftChildIdx]:
        largestIdx = rightChildIdx

    if heap[largestIdx] > heap[currentIdx]:
        swap(heap, currentIdx, largestIdx)
        siftDown2(heap, largestIdx, endIdx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(heapSort(array))
