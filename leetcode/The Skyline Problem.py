# https://leetcode.com/problems/the-skyline-problem/

import heapq

# Time: O(nlogn) | Space: O(n)
def getSkyline(buildings):
    n = len(buildings)
    curr_max = curr_i = next_building = 0
    maxheap, result = [], []
    while maxheap or next_building < n:
        while next_building < n and curr_i == buildings[next_building][0]:
            left, right, height = buildings[next_building]
            next_building += 1
            heapq.heappush(maxheap, (-height, left, right))
        while maxheap and curr_i >= maxheap[0][2]:
            heapq.heappop(maxheap)
        new_max = -maxheap[0][0] if maxheap else 0
        if new_max != curr_max:
            result.append([curr_i, new_max])
        curr_max = new_max
        next_stop = float("inf")
        if next_building < n:
            next_stop = min(next_stop, buildings[next_building][0])
        if maxheap:
            next_stop = min(next_stop, maxheap[0][2])
        curr_i = next_stop
    return result



buildings = [[0,2147483647,2147483647]]

print(getSkyline(buildings))