# def longestSubstringWithoutDuplication(string):
#     lastSeen = {}
#     startingIdx = 0
#     longest = [0, 1]
#     for idx, char in enumerate(string):
#         if char in lastSeen:
#             startingIdx = max(startingIdx, lastSeen[char]+1)

#         if longest[1] - longest[0] < idx+1-startingIdx:
#             longest = [startingIdx, idx+1]

#         lastSeen[char] = idx

#     return string[longest[0]:longest[1]]

def longestSubstringWithoutDuplication(string):
    if not string:
        return ""

    charIndex = {}
    startIdx = 0
    longestSubString = ""
    for idx, char in enumerate(string):
        if char in charIndex and charIndex[char] >= startIdx:
            startIdx = charIndex[char] + 1

        currentLength = idx - startIdx
        if currentLength > len(longestSubString):
            longestSubString = string[startIdx:idx+1]

        charIndex[char] = idx

    return longestSubString


string = "clementisacap"
print(longestSubstringWithoutDuplication(string))
