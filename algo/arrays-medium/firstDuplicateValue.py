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
    for value in array: 
        absValue = abs(value) 
        if array[absValue - 1] < 0: 
            return absValue 
        array[absValue - 1] = -array[absValue - 1] 
    return -1


array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))
