def minNumberOfCoinsForChange(n, denoms):
    dp = [float("Inf")] * (n+1)
    dp[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if amount < denom:
                continue

            # 1代表当前面额硬币的数量
            # amount-denom代表减掉当前面额之后还剩的硬币数量
            # 两者相加即为本次计算出的硬币数量
            dp[amount] = min(dp[amount], 1+dp[amount-denom])

    return dp[n] if dp[n] != float("Inf") else -1


n = 7
denoms = [1, 5]
print(minNumberOfCoinsForChange(n, denoms))
