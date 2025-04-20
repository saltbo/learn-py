def selectionSort(array):
    newArray = []
    while (len(array) > 0):
        minimum = min(array)
        newArray.append(minimum)
        array.remove(minimum)

    return newArray


def selectionSort2(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        minimumIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[i] < array[minimumIdx]:
                minimumIdx = i
        swap(minimumIdx, currentIdx, array)

        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
sortedArray = selectionSort2(array)
print(sortedArray)
