def riverSizes(matrix):
    rowLength = len(matrix)
    colLength = len(matrix[0])

    sizes = []
    visited = set()
    for rowIdx in range(rowLength):
        for colIdx in range(colLength):
            if (rowIdx, colIdx) not in visited and matrix[rowIdx][colIdx] == 1:
                sizes.append(dfs(matrix, rowIdx, colIdx, visited))

    return sizes


def dfs(matrix, rowIdx, colIdx, visited: set):
    if (rowIdx not in range(len(matrix)) or colIdx not in range(len(matrix[0])) or
            matrix[rowIdx][colIdx] == 0 or (rowIdx, colIdx) in visited):
        return 0

    visited.add((rowIdx, colIdx))

    size = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        size += dfs(matrix, rowIdx+dx, colIdx+dy, visited)

    return size+1


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
print(riverSizes(matrix))
