def searchInSortedMatrix(matrix, target):
    x, y = 0, len(matrix[0])-1
    print(x, y)

    while x < len(matrix) and y >= 0:
        print(x, y)
        value = matrix[x][y]
        if value == target:
            return [x, y]

        if value > target:
            y -= 1
        elif value < target:
            x += 1

    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
target = 1
print(searchInSortedMatrix(matrix, target))
