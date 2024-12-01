def commonCharacters(strings):
    map = {}
    for str in strings:
        for s in list(set(str)):
            if s not in map:
                map[s] = 1
                continue
            map[s] += 1

    result = []
    for key in map:
        if map[key] >= len(strings):
            result.append(key)
    return result

strings = ["abc", "bed", "cbaced"]
print(commonCharacters(strings))