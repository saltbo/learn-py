def lengthOfLongestSubstring(s: str):
    length = 0
    left = 0

    memory = dict()
    for right in range(len(s)):
        char = s[right]
        if char in memory and memory[char] >= left:
            left = memory[char] + 1
        memory[char] = right
        length = max(length, right-left+1)

    return length


print(lengthOfLongestSubstring(" "))
print("----")
print(lengthOfLongestSubstring("abcabcbb"))
