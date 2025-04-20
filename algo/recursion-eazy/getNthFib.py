def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib(n-1) + getNthFib(n-2)


def getNthFibWithCache(n, cache={1: 0, 2: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = getNthFibWithCache(
            n-1, cache)+getNthFibWithCache(n-2, cache)
        return cache[n]


def getNthFib2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    count = 3
    subseq = [0, 1]
    while (count<=n):
        next = subseq[0]+subseq[1]
        subseq[0] = subseq[1]
        subseq[1] = next
        count+=1
    return subseq[1]


# v = getNthFib(6)
# v = getNthFibWithCache(6)
v = getNthFib2(6)
print(v)
