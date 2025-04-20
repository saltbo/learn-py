def bubbleSort(array):
    index = 0
    currentLen = len(array)
    while (currentLen > 0):
        if index == len(array) - 1:
            index = 0
            currentLen -= 1
            continue

        current = array[index]
        nextValue = array[index+1]
        if current > nextValue:
            array[index] = nextValue
            array[index+1] = current
            print(array)

        index += 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
sortedArray = bubbleSort(array)
print(sortedArray)
