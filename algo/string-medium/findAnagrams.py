from collections import Counter
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []

    p_count = Counter(p)
    print(p_count)

    result = []
    window_count = Counter(s[:len(p)])
    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # 向右扩展一个位置（添加右侧新字符）
        window_count[s[i]] += 1

        # 向右移动起始位置（移除左侧旧字符）
        left_char = s[i-len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        # 判断新窗口内的词频
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result


print(findAnagrams("cbaebabacd", "abc"))
