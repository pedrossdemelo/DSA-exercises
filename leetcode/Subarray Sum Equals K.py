# https://leetcode.com/problems/subarray-sum-equals-k/

from bisect import bisect_left
from collections import defaultdict


# Time: O(n) | Space: O(n)
def subarraySum(nums, k):
    sumsToK = 0
    prefixSum = []
    pSumIndexes = defaultdict(list)
    pSumIndexes[0].append(-1)
    for i, num in enumerate(nums):
        prefixSum.append(num + (prefixSum[-1] if prefixSum else 0))
        pSumIndexes[prefixSum[-1]].append(i)

    for i, psum in enumerate(prefixSum):
        target = psum - k
        if target in pSumIndexes:
            lessthan_i = bisect_left(pSumIndexes[target], i)
            sumsToK += lessthan_i

    return sumsToK

nums = [1,1,1]; k = 2
print(subarraySum(nums, k))