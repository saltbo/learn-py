def firstDuplicateValue(array):
    m = {}
    for num in array:
        if num not in m:
            m[num] = 1
        else:
            return num
    return -1


def firstDuplicateValue2(array):
    appears = set()
    for num in array:
        if num not in appears:
            appears.add(num)
        else:
            return num
    return -1


def firstDuplicateValue3(array):
    for num in array:
        absNum = abs(num)
        if array[absNum-1] < 0:
            return absNum
        array[absNum-1] = -array[absNum-1]
    return -1


array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))
