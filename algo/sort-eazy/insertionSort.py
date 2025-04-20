def insertionSort(array):
    for idx in range(1, len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            array[idx], array[idx-1] = array[idx-1], array[idx]
            idx -= 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
sortedArray = insertionSort(array)
print(sortedArray)
