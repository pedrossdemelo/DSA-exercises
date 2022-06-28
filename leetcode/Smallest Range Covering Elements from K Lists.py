# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from heapq import heapify, heappop, heappush
from typing import List

# n = len(nums)
# m = min(len(arr) for arr in nums)
# Time: O(nmlogn) | Space: O(n)
def smallestRange(nums: List[List[int]]) -> List[int]:
    n, rangeend, rangeheap = len(nums), float("-inf"), []
    for i in range(n):
        rangeheap.append((nums[i][0], i, 0))
        rangeend = max(rangeend, nums[i][0])
    heapify(rangeheap)

    result = [float("inf"), None, None]

    while True:
        rangestart, nums_i, list_i = heappop(rangeheap)
        if rangeend - rangestart < result[0]:
            result = [rangeend - rangestart, rangestart, rangeend]
        list_i += 1
        if list_i < len(nums[nums_i]):
            rangeend = max(rangeend, nums[nums_i][list_i])
            heappush(rangeheap, (nums[nums_i][list_i], nums_i, list_i))
        else:
            break

    return result[1:]

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(smallestRange(nums))