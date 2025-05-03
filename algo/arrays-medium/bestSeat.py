def bestSeat(seats):
    currentZeroCount = 0
    longestZeroCount = 0
    longestZeroChainEndAt = 0
    for idx, seat in enumerate(seats):
        if seat == 0:
            currentZeroCount += 1
        else:
            currentZeroCount = 0

        if currentZeroCount > longestZeroCount:
            longestZeroChainEndAt = idx
            longestZeroCount = currentZeroCount

    return longestZeroChainEndAt - longestZeroCount//2 if longestZeroCount > 0 else -1


# seats = [1, 0, 1, 0, 0, 0, 1]
seats = [1, 1, 1, 1]

print(bestSeat(seats))
