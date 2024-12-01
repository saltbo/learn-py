
def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1

    minimum = 0
    sortedCoins = sorted(coins)
    for coin in sortedCoins:
        if coin > minimum + 1:
            break
        minimum += coin

    return minimum + 1


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
# output: 20

# 解题原理：
# 如果遍历过的所有硬币累加都够不上下一个硬币的面值，那么小于下一个硬币的面值的金额就无法作为零钱找出去。
# 在示例中前几个加起来总数为19，那么22 21 20就都找不出去，即最小不可找零金额为20。
