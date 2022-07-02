from collections import Counter
from typing import List

# Time: O(n!) | Space: O(n)
def permuteUnique(nums: List[int]) -> List[List[int]]:
    counter = Counter(nums)
    result, curr = [], []
    def dfs():
        if len(curr) == len(nums):
            result.append(curr.copy())
        for val, count in counter.most_common():
            counter[val] -= 1
            curr.append(val)
            if counter[val] == 0:
                del counter[val]
            dfs()
            curr.pop()
            counter[val] += 1
    dfs()
    return result

nums = [1,1,2]
print(permuteUnique(nums))

