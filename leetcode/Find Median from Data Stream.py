# https://leetcode.com/problems/find-median-from-data-stream/


from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.upperhalf = []
        self.lowerhalf = []

    def addNum(self, num: int) -> None:
        if len(self.upperhalf) == len(self.lowerhalf):
            heappush(self.upperhalf, -heappushpop(self.lowerhalf, -num))
        else:
            heappush(self.lowerhalf, -heappushpop(self.upperhalf, num))

    def findMedian(self) -> float:
        if len(self.upperhalf) == len(self.lowerhalf):
            return (self.upperhalf[0] - self.lowerhalf[0]) / 2
        else:
            return self.upperhalf[0]

methods = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
args = [[], [1], [2], [], [3], []]
expected = [None, None, None, 1.5, None, 2.0]

mf = MedianFinder(*args[0])

for method, arg, expect in zip(methods[1:], args[1:], expected[1:]):
    res = getattr(mf, method)(*arg)
    print(f"{res} | {expect}")
