def minimumWaitingTime(queries):
    queries.sort()

    waitingTime = 0
    for idx, query in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        waitingTime += query * queriesLeft
    return waitingTime


queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))
