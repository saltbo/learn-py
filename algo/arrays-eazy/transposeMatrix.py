def transposeMatrix(matrix):
    newMatrix = []
    for colIdx in range(len(matrix[0])):
        newRow = []
        for rowIdx in range(len(matrix)):
            newRow.append(matrix[rowIdx][colIdx])
        newMatrix.append(newRow)
    return newMatrix

matrix = [
    [1,2,3],
    [2,3,4]
]
print(transposeMatrix(matrix))
# output:
# output = [
#     [1, 2], 
#     [2, 3], 
#     [3, 4]
# ]

# 解题思路：把每一列取出来变成新的行