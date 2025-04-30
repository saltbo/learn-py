def reverseWordsInString(string):
    words = split(string, " ")
    reverse(words)
    return " ".join(words)


def reverse(list):
    left = 0
    right = len(list)-1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1


def split(string, sep):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == sep:
            words.append(string[startOfWord:idx])
            startOfWord = idx+1

    words.append(string[startOfWord:])
    return words


string = "AlgoExpert is the best!"
print(reverseWordsInString(string))
print(split(string, " "))
