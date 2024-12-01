def semordnilap(words):
    wordSet = set(words)
    results = []
    for word in words:
        reversedWord = word[::-1]
        if reversedWord in wordSet and reversedWord != word:
            results.append([word, reversedWord])
            wordSet.remove(word)
            wordSet.remove(reversedWord)

    return results


words = ["dog", "god"]
semordnilap(words)
