# O(n + m) time | O(n + m) space
# def oneEdit(stringOne, stringTwo):
#     lenOne, lenTwo = len(stringOne), len(stringTwo)
#     if abs(lenOne-lenTwo) > 1:
#         return False

#     for i in range(min(lenOne, lenTwo)):
#         if stringOne[i] != stringTwo[i]:
#             if lenOne > lenTwo:
#                 return stringOne[i+1:] == stringTwo[i:]
#             elif lenTwo> lenOne:
#                 return stringTwo[i+1:] == stringOne[i:]
#             else:
#                 return stringOne[i+1:] == stringTwo[i+1:]
#     return True

def oneEdit(stringOne, stringTwo):
    lenOne, lenTwo = len(stringOne), len(stringTwo)
    if abs(lenOne-lenTwo) > 1:
        return False

    else:
        i, j, diff = 0, 0, 0
        while i < lenOne and j < lenTwo:
            if stringOne[i] == stringTwo[j]:
                # 相同就同时移动指针
                i += 1
                j += 1
            else:
                # 如果不同就哪个长移动哪个指针
                diff += 1
                if lenOne > lenTwo:
                    i += 1
                elif lenTwo > lenOne:
                    j += 1
                else:
                    i += 1
                    j += 1
        # 如果差异超过两个就不可能一次编辑完成目标了
        return diff < 2


stringOne = "hello"
stringTwo = "helo"
print(oneEdit(stringOne, stringTwo))
