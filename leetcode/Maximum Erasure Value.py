from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    cumulative = []
    for num in nums:
        cumulative.append(num + (cumulative[-1] if cumulative else 0))
    lastseen = {}
    start = currsum = maxsum = 0
    for i, num in enumerate(nums):
        if num in lastseen and lastseen[num] >= start:
            start = lastseen[num] + 1
            currsum = cumulative[i] - cumulative[start - 1]
        else:
            currsum += num
            maxsum = max(maxsum, currsum)
        lastseen[num] = i
    return maxsum


nums = [4,2,4,5,6]

print(maximumUniqueSubarray(nums))