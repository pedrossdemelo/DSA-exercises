# https://leetcode.com/problems/move-zeroes/

from typing import List


# Time: O(n) | Space: O(1)
def moveZeroes(nums: List[int]) -> None:
    last_0 = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[last_0], nums[i] = nums[i], nums[last_0]
            last_0 += 1


nums = [9, 1, 0, 3, 12, 0]
moveZeroes(nums)
print(nums)
