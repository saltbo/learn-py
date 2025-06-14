def globMatching(fileName, pattern):
    fileNameLen, patternLen = len(fileName), len(pattern)

    # initialize DP table
    dp = [[False for _ in range(patternLen + 1)]
          for _ in range(fileNameLen + 1)]

    # empty pattern matches empty fileName
    dp[0][0] = True

    # pattern starts with '*' can match empty fileName
    for pIdx in range(1, patternLen + 1):
        if pattern[pIdx - 1] == '*':
            dp[0][pIdx] = dp[0][pIdx - 1]

    # fill the DP table
    for fnIdx in range(1, fileNameLen + 1):
        for pIdx in range(1, patternLen + 1):
            if pattern[pIdx - 1] == '*':
                # '*' can match zero or more characters
                dp[fnIdx][pIdx] = dp[fnIdx][pIdx - 1] or dp[fnIdx - 1][pIdx]
            elif pattern[pIdx - 1] == '?' or pattern[pIdx - 1] == fileName[fnIdx - 1]:
                # '?' matches any single character, or characters match exactly
                dp[fnIdx][pIdx] = dp[fnIdx - 1][pIdx - 1]

    return dp[fileNameLen][patternLen]


pattern = "*"
fileName = "abcdegh"
print(globMatching(fileName, pattern))
