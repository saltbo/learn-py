def kadanesAlgorithm(array):
    sumUp = float("-inf")
    maximumSumUp = float("-inf")
    for num in array:
        sumUp = max(num, sumUp+num)
        maximumSumUp = max(maximumSumUp, sumUp)

    return maximumSumUp


# array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
array = [-2, -1]
print(kadanesAlgorithm(array))
