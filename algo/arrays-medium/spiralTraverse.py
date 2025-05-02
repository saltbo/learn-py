def spiralTraverse(array):
    startingRow = 0
    startingCol = 0
    endingRow = len(array)-1
    endingCol = len(array[0])-1

    result = []
    print(len(result), len(array)*len(array[0]))
    exceptLen = len(array)*len(array[0])
    while len(result) < exceptLen:
        for col in range(startingRow, endingCol+1):
            result.append(array[startingRow][col])
        print(result)

        for row in range(startingRow+1, endingRow+1):
            result.append(array[row][endingCol])
        print(result)

        if len(result) == exceptLen:
            break

        for col in range(endingCol-1, startingCol, -1):
            print(endingRow-1, col)
            result.append(array[endingRow][col])
        print(result)

        for idx in range(endingRow, startingRow, -1):
            result.append(array[idx][startingCol])
        print(result)

        startingRow += 1
        startingCol += 1
        endingRow -= 1
        endingCol -= 1
    return result


array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]

    # [27, 12, 35, 26],
    # [25, 21, 94, 11],
    # [19, 96, 43, 56],
    # [55, 36, 10, 18],
    # [96, 83, 31, 94],
    # [93, 11, 90, 16]
]

print(spiralTraverse(array))
