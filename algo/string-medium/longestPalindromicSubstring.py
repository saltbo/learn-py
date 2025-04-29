def longestPalindromicSubstring(string):
    longest = ""
    for left in range(len(string)):
        for right in range(left+1, len(string)+1):
            if isPalindromic(string, left, right) and right-left > len(longest):
                longest = string[left:right]

    return longest


def isPalindromic(string, left, right):
    return string[left:right] == string[left:right][::-1]


string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))
