# https://leetcode.com/problems/furthest-building-you-can-reach/

# n = len(heights) | k = bricks + ladders
from heapq import heappop, heappush

# Time: O(nlogn) | Space: O(n)
def furthestBuilding(heights, bricks, ladders):
    maxheap, i = [], 0
    while i < len(heights) - 1:
        elevation = heights[i + 1] - heights[i]
        if elevation <= 0:
            i += 1
            continue
        if bricks >= elevation:
            bricks -= elevation
            heappush(maxheap, -elevation)
        elif ladders:
            ladders -= 1
            if maxheap and -maxheap[0] > elevation:
                bricks += -heappop(maxheap)
                continue
        else:
            break
        i += 1
    return i


heights, bricks, ladders = ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)

print(furthestBuilding(heights, bricks, ladders))
