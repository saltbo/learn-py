def threeNumberSort(array, order):
    newArray = []
    for o in order:
        for n in array:
            if n == o:
                newArray.append(n)
    return newArray


def threeNumberSort1(array, order):
    elementCounts = [0, 0, 0]
    for element in array:
        index = order.index(element)
        elementCounts[index] += 1

    current = 0
    for idx, n in enumerate(elementCounts):
        print(n)
        if n == 0:
            continue

        for i in range(n):
            array[current] = order[idx]
            current += 1

    return array


def threeNumberSort2(array, order):
    firstIdx = 0
    firstElement = order[0]
    lastIdx = len(array)-1
    lastElement = order[len(order)-1]
    for i in range(len(array)):
        if array[i] == firstElement:
            swap(i, firstIdx, array)
            firstIdx += 1

    for i in range(len(array)-1, 0, -1):
        print(i)
        if array[i-1] == lastElement:
            swap(i-1, lastIdx, array)
            lastIdx -= 1

    return array


def threeNumberSort3(array, order):
    firstIdx = 0
    firstElement = order[0]
    secondIdx = 0
    thirdIdx = len(array)-1
    thirdElement = order[2]
    while (secondIdx < thirdIdx):
        if array[secondIdx] == firstElement:
            swap(secondIdx, firstIdx, array)
            firstIdx += 1
            secondIdx += 1
        elif array[secondIdx] == thirdElement:
            swap(secondIdx, thirdIdx, array)
            thirdIdx -= 1
        else:
            secondIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
# array = [-2, -3, -3, -3, -3, -3, -2, -2, -3]
# order = [-2, -3, 0]
# array = [1, 2, 3]
# order = [3, 1, 2]
# array = [0, 1]
# order = [1, 2, 0]
sortedArray = threeNumberSort1(array, order)
print(sortedArray)
