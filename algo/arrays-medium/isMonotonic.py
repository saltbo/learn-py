def isMonotonic(array):
    if len(array) < 2:
        return True

    previousNum = array[0]
    previousDirect = ""
    currentDirect = ""
    for idx in range(1, len(array)):
        if array[idx] > previousNum:
            currentDirect = "up"
        elif array[idx] < previousNum:
            currentDirect = "down"
        previousNum = array[idx]

        if previousDirect == "":
            previousDirect = currentDirect
        elif previousDirect != currentDirect:
            return False

    return True


def isMonotonic2(array):
    if len(array) < 2:
        return True

    isIncreasing = True
    isDecreasing = True
    for idx in range(1, len(array)):
        if array[idx] > array[idx-1]:
            isDecreasing = False
        elif array[idx] < array[idx-1]:
            isIncreasing = False

    return isIncreasing or isDecreasing


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic2(array))
