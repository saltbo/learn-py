def longestPalindromicSubstring(string):
    longest = ""
    for left in range(len(string)):
        for right in range(left+1, len(string)+1):
            if isPalindromic(string, left, right) and right-left > len(longest):
                longest = string[left:right]

    return longest


def isPalindromic(string, left, right):
    return string[left:right] == string[left:right][::-1]


def longestPalindromicSubstring2(s):
    longest = ""
    for i in range(len(s)):
        odd = expandAroundCenter(s, i, i)
        even = expandAroundCenter(s, i, i+1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    print(left, right)
    return s[left+1:right]


string = "abaxyzzyxf"
# print(expandAroundCenter(string, 5, 6))
print(longestPalindromicSubstring2(string))
# print(longestPalindromicSubstring(string))
