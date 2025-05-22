# def numberOfWaysToTraverseGraph(width, height):
#     if width == 1 or height == 1:
#         return 1

#     return numberOfWaysToTraverseGraph(width, height-1)+numberOfWaysToTraverseGraph(width-1, height)


def numberOfWaysToTraverseGraph(width, height):
    dp = [[0 for _ in range(width+1)] for _ in range(height+1)]
    for row in dp:
        print(row)
    print("="*10)
    for widthIdx in range(1, width+1):
        for heightIdx in range(1, height+1):
            if widthIdx == 1 or heightIdx == 1:
                dp[heightIdx][widthIdx] = 1
            else:
                dp[heightIdx][widthIdx] = dp[heightIdx-1][widthIdx] + \
                    dp[heightIdx][widthIdx-1]
    for row in dp:
        print(row)
    return dp[height][width]


print(numberOfWaysToTraverseGraph(4, 2))
