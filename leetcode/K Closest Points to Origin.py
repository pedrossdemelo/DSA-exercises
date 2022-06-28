# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heapify, heapreplace
from math import sqrt

# Time: O(nlogk) | Space: O(k)
def kClosest(points, k):
    n = len(points)
    maxheap = [(-sqrt(points[i][0] ** 2 + points[i][1] ** 2), i) for i in range(k)]
    heapify(maxheap)
    for i in range(k, n):
        distance = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        if distance < -maxheap[0][0]:
            heapreplace(maxheap, (-distance, i))
    return [points[i] for _, i in maxheap]


points = [[3, 3], [5, -1], [-2, 4], [1, 1], [5, 9]]
k = 2

print(kClosest(points, k))
