def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)

    idxOne = 0
    idxTwo = 0
    smallestDiff = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        currentDiff = 0
        firstNum, secondNum = arrayOne[idxOne], arrayTwo[idxTwo]
        if firstNum == secondNum:
            smallestPair = [firstNum, secondNum]
            break
        elif firstNum > secondNum:
            currentDiff = firstNum - secondNum
            idxTwo += 1
        elif secondNum > firstNum:
            currentDiff = secondNum - firstNum
            idxOne += 1

        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            smallestPair = [firstNum, secondNum]

    return smallestPair


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))
