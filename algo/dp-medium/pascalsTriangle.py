def pascalsTriangle(numRows):
    if numRows < 0:
        return []

    triangle = [[1]]
    for rowIdx in range(1, numRows):
        prevRow = triangle[rowIdx-1]

        newRow = [1] * (rowIdx + 1)
        for j in range(1, rowIdx):
            newRow[j] = prevRow[j-1]+prevRow[j]

        triangle.append(newRow)
    return triangle


print(pascalsTriangle(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
