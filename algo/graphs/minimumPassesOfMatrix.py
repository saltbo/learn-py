def minimumPassesOfMatrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    # 辅助函数: 判断坐标是否在矩阵范围内
    def inBounds(row, col):
        return 0 <= row < ROWS and 0 <= col < COLS

    # 收集所有正数位置
    def collectPositives():
        positions = []
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] > 0:
                    positions.append((r, c))
        return positions

    # 执行一次传递，将负数转为正数
    def convert(currentPositives):
        newPositives = []
        converted = False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r, c in currentPositives:
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if inBounds(nr, nc) and matrix[nr][nc] < 0:
                    matrix[nr][nc] *= -1
                    newPositives.append((nr, nc))
                    converted = True

        return newPositives, converted

    # 检查矩阵中是否还有负数
    def hasNegatives():
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] < 0:
                    return True

        return False

    # 主逻辑
    passes = 0
    positives = collectPositives()
    while positives:
        positives, converted = convert(positives)
        if converted:
            passes += 1

    return -1 if hasNegatives() else passes


matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

print(minimumPassesOfMatrix(matrix))
