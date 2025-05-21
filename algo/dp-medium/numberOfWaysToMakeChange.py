def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n+1)
    ways[0] = 1
    for denom in denoms:
        print(denom)
        for amount in range(1, n+1):
            if denom > amount:
                continue

            ways[amount] += ways[amount-denom]
        print(ways)

    return ways[n]


n = 6
denoms = [1, 5]
print(numberOfWaysToMakeChange(n, denoms))
