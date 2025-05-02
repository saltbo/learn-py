def minimumCharactersForWords(words):
    characters = {}
    for word in words:
        wordCounts = dict.fromkeys(word, 0)
        for character in word:
            wordCounts[character] += 1

        for w, count in wordCounts.items():
            if w not in characters:
                characters[w] = 0

            previousCount = characters[w]
            if int(previousCount) < count:
                characters[w] = count

    minimumCharacters = []
    for character, count in characters.items():
        for _ in range(count):
            minimumCharacters.append(character)

    return minimumCharacters


words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))
