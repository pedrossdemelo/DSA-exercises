from typing import List

# Time: O(n) | Space: O(1)
def findUnsortedSubarray(nums: List[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1
    start = end = 0
    minn, maxn = nums[right], nums[left]

    while left < n and right >= 0:
        leftn, rightn = nums[left], nums[right]
        if leftn < maxn:
            end = left + 1
        if rightn > minn:
            start = right
        maxn = max(maxn, leftn)
        minn = min(minn, rightn)
        left += 1
        right -= 1

    return end - start


nums = [1, 2, 3, -1, 4]
print(findUnsortedSubarray(nums))
