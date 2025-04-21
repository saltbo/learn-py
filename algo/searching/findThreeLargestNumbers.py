def findThreeLargestNumbers(array):
    largestNumbers = [None, None, None]

    for num in array:
        if largestNumbers[2] is None or num > largestNumbers[2]:
            largestNumbers[0] = largestNumbers[1]
            largestNumbers[1] = largestNumbers[2]
            largestNumbers[2] = num
        elif largestNumbers[1] is None or num > largestNumbers[1]:
            largestNumbers[0] = largestNumbers[1]
            largestNumbers[1] = num
        elif largestNumbers[0] is None or num > largestNumbers[0]:
            largestNumbers[0] = num
    return largestNumbers


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))
