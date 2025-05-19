def removeIslands(matrix):
    # 检查矩阵的边界并开始DFS
    rows, cols = len(matrix), len(matrix[0])
    for rIdx in range(rows):
        for cIdx in range(cols):
            # 如果不是边界或者值不为1，则跳过
            isOnBorder = rIdx == 0 or rIdx == rows-1 or cIdx == 0 or cIdx == cols-1
            if not isOnBorder or matrix[rIdx][cIdx] != 1:
                continue
            dfs(matrix, rIdx, cIdx)

    # 将所有剩余的1（岛屿）变为0，将2（边界连接的1）恢复为1
    for rIdx in range(rows):
        for cIdx in range(cols):
            if matrix[rIdx][cIdx] == 0:
                continue
            matrix[rIdx][cIdx] -= 1

    return matrix


# 使用DFS标记所有与边界相连的1为2
def dfs(matrix, r, c):
    rows, cols = len(matrix), len(matrix[0])
    # 边界条件检查
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    if matrix[r][c] != 1:
        return

    matrix[r][c] += 1

    dfs(matrix, r-1, c)
    dfs(matrix, r+1, c)
    dfs(matrix, r, c-1)
    dfs(matrix, r, c+1)


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

result = removeIslands(matrix)
for row in result:
    print(row)
