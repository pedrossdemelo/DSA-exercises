# https://leetcode.com/problems/find-k-closest-elements/


import heapq


def findClosestElements(arr, k, x):
    n, i = len(arr), -1
    left, right = 0, n - 1
    while left <= right: # O(logn)
        mid = (left + right) // 2
        if arr[mid] == x:
            i = mid
            break
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    i = i if i >= 0 else left

    maxheap = []
    idxs = set()
    candidaterange = range(max(i-k, 0), min(i+k, n))
    for j in candidaterange: # O(klogk)
        diff = abs(arr[j] - x)
        if len(maxheap) < k:
            heapq.heappush(maxheap, (-diff, arr[j], j))
            idxs.add(j)
        elif -diff > -maxheap[0][0]:
            idxs.remove(heapq.heapreplace(maxheap, (-diff, arr[j], j))[2])
            idxs.add(j)

    return [arr[i] for i in candidaterange if i in idxs] #O(k)

arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5

print(findClosestElements(arr, k, x))
