def groupAnagrams(words):
    anagrams = dict()
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# print(groupAnagrams(words))

sortedWords = ["".join(sorted(w)) for w in words]
indices = [i for i in range(len(words))]
print(indices)
indices.sort(key=lambda x: sortedWords[x])
print(indices)

