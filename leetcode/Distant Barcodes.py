# https://leetcode.com/problems/distant-barcodes/

from collections import Counter
from heapq import heapify, heappop, heappush


# Time: O(nlogn) | Space: O(n)
def rearrangeBarcodes(barcodes):
    heap = [(-count, num) for num, count in Counter(barcodes).most_common()]
    heapify(heap)
    result = []

    while heap:
        c1, n1 = heappop(heap)
        c2, n2 = heappop(heap) if heap else (0, None)
        result.append(n1)
        if not n2: break
        result.append(n2)
        if -c1 > 1:
            heappush(heap, (c1+1, n1))
        if -c2 > 1:
            heappush(heap, (c2+1, n2))

    return result

print(rearrangeBarcodes([1,1,1,1,2,2,2,3]))