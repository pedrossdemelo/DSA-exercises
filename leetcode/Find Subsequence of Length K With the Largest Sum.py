# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

import heapq

# Time: O(nlogk) | Space: O(k)
def maxSubsequence(nums, k):
    n = len(nums)  # O(1)
    heap = [(nums[i], i) for i in range(k)]  # O(k)
    heapq.heapify(heap)  # O(k)
    indexes = {i for i in range(k)}  # O(k)
    for i in range(k, n):  # O((n-k)logk)
        if nums[i] > heap[0][0]:
            indexes.add(i)
            indexes.remove(heapq.heapreplace(heap, (nums[i], i)))
    return [nums[i] for i in range(n) if i in indexes]  # O(n)
