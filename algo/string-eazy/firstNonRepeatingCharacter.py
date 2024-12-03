from collections import defaultdict

def firstNonRepeatingCharacter(string):
    dict = defaultdict(int)
    for s in string:
        dict[s] += 1

    for idx in range(len(string)):
        if dict[string[idx]] == 1:
            return idx
        
    return -1

print(firstNonRepeatingCharacter("faadabcbbebdf"))