from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    count = 0

    sum_map = {0: 1}  # 前缀和及其出现次数的映射
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if (curr_sum - k) in sum_map:
            count += 1
        sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1

    print(sum_map)
    return count


print(subarraySum([1, 1, 1], 2))
print("-----")
print(subarraySum([1, 2, 3], 3))
