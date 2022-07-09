# https://leetcode.com/problems/array-nesting/submissions/

from typing import List


# Time: O(n) | Space: O(1)
def arrayNesting(nums: List[int]) -> int:
    # This a graph cycle size problem
    # [5,4,0,3,1,6,2]
    # 0 -> 5 -> 6 -> 2 -> ...0 # size 4
    # 3 -> ...3 # size 1
    # 1 -> 4 -> ...1 # size 2
    n = len(nums)
    result = 0
    VISITED = -1
    for i in range(n):
        cyclelength = 0
        curr = nums[i]
        while nums[curr] is not VISITED:
            temp = nums[curr]
            nums[curr] = VISITED
            curr = temp
            cyclelength += 1
        result = max(result, cyclelength)
    return result

print(arrayNesting([5,4,0,3,1,6,2]))