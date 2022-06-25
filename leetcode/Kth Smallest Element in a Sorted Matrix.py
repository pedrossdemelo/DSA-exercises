# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq
from typing import List

# Time: O(n**2logk) | Space: O(k)
def kthSmallest(matrix: List[List[int]], k: int):
    maxheap = []
    for row in matrix:
        for val in row:
            if len(maxheap) < k:
                heapq.heappush(maxheap, -val)
            elif -maxheap[0] > val:
                heapq.heapreplace(maxheap, -val)
    return -maxheap[0]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(kthSmallest(matrix, k))
