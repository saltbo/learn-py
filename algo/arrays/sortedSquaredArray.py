def sortedSquaredArray(array):
    squared = []
    for num in array:
        squared.append(num*num)
    return sorted(squared)


def sortedSquaredArray2(array):
    leftIdx = 0
    rightIdx = len(array) - 1
    newArr = [0 for _ in array]
    for idx in reversed(range(len(array))):
        leftValue = array[leftIdx]
        rightValue = array[rightIdx]
        if abs(leftValue) > abs(rightValue):
            newArr[idx] = leftValue * leftValue
            rightIdx += 1
        else:
            newArr[idx] = rightValue * rightValue
            leftIdx += 1
        
    return newArr

print(sortedSquaredArray2([1, 2, 3, 5, 6, 8, 9]))