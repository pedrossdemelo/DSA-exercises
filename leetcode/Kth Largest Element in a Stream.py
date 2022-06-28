# https://leetcode.com/problems/kth-largest-element-in-a-stream/


from heapq import heappush, heapreplace


class KthLargest:
    def __init__(self, k, nums) -> None:
        self.klargest = []
        self.k = k
        for val in nums:
            if len(self.klargest) < self.k:
                heappush(self.klargest, val)
            elif self.klargest[0] < val:
                heapreplace(self.klargest, val)

    def add(self, val):
        if len(self.klargest) < self.k:
            heappush(self.klargest, val)
        elif self.klargest[0] < val:
            heapreplace(self.klargest, val)
        return self.klargest[0]


methods, args, expected = (
    ["KthLargest", "add", "add", "add", "add", "add"],
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
    [None, 4, 5, 5, 8, 8]
)

kth = KthLargest(*args[0])

for method, arg, expect in zip(methods[1:], args[1:], expected[1:]):
    res = getattr(kth, method)(*arg)
    print(f"{res} | {expect}")
