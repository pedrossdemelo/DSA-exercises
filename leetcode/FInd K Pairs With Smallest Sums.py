# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import heapq
from random import randrange

# n = len(nums1), m = len(nums2)
# p = max(n, m, k)
# q = min(n * m, k)
# Space: O(p) | Time: O(qlogz)
def kSmallestPairs(nums1, nums2, k):
    N1, N2 = len(nums1), len(nums2)
    candidates = [(nums1[0] + nums2[0], (0, 0))]
    result = []
    maxspace = 0
    while k and candidates:
        maxspace = max(maxspace, len(candidates))
        n1i, n2i = heapq.heappop(candidates)[1]
        result.append((nums1[n1i], nums2[n2i]))
        if n1i < N1 - 1:
            heapq.heappush(candidates, (nums1[n1i + 1] + nums2[n2i], (n1i + 1, n2i)))
        if n2i < N2 - 1 and n1i == 0:
            heapq.heappush(candidates, (nums1[n1i] + nums2[n2i + 1], (n1i, n2i + 1)))
        k -= 1
    return len(result), maxspace


nums1 = sorted(randrange(0, 100000) for _ in range(1000))
nums2 = sorted(randrange(0, 100000) for _ in range(10000))
k = 2
print(kSmallestPairs(nums1, nums2, float("inf")))
