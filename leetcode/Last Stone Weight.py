# https://leetcode.com/problems/last-stone-weight/

# Time: O(nlogn) | Space: O(n)
from heapq import heapify, heappop, heappush


def lastStoneWeight(stones):
    maxheap = [-stone for stone in stones]
    heapify(maxheap)
    while len(maxheap) > 1:
        smashed = -heappop(maxheap) - -heappop(maxheap)
        if smashed == 0:
            continue
        heappush(maxheap, -smashed)
    return -maxheap[0]


stones = [2, 7, 4, 1, 8, 99]
print(lastStoneWeight(stones))
