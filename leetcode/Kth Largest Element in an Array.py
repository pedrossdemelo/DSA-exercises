# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

# Time: O(nlogk) | Space: O(k)
def findKthLargest(nums, k):
    heap = []
    for num in nums:  # worst case all numbers are sorted
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return heapq.heappop(heap)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))
