# https://leetcode.com/problems/dinner-plate-stacks/

from heapq import heappush, heappop


class heap:
    def __init__(self, max=False) -> None:
        self.heap = []
        self.indexof = {}

    def __len__(self):
        return len(self.heap)

    def __repr__(self) -> str:
        return str(self.heap)

    def __getitem__(self, item):
        return self.heap[item]

    def swap(self, i, j):
        n = len(self)
        i, j = i if i >= 0 else n + i, j if j >= 0 else n + j
        self.indexof[self.heap[i]], self.indexof[self.heap[j]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def c(self, i):
        l, r = i * 2 + 1, i * 2 + 2
        if l >= len(self):
            return None
        if r >= len(self):
            return l
        return r if self.heap[r] < self.heap[l] else l

    def p(self, i):
        p = (i - 1) // 2
        return p if p >= 0 else None

    def siftup(self, i):
        while self.p(i) is not None and self.heap[self.p(i)] > self.heap[i]:
            p = self.p(i)
            self.swap(p, i)
            i = p

    def siftdown(self, i):
        while self.c(i) is not None and self.heap[self.c(i)] < self.heap[i]:
            c = self.c(i)
            self.swap(c, i)
            i = c

    def pop(self):
        if not self.heap:
            raise IndexError()
        self.swap(0, -1)
        val = self.heap.pop()
        self.siftdown(0)
        del self.indexof[val]
        return val

    def push(self, val):
        self.heap.append(val)
        self.indexof[val] = len(self) - 1
        self.siftup(self.indexof[val])

    def remove(self, val):
        if val not in self.indexof:
            raise IndexError(f"{val} not in heap")
        i = self.indexof[val]
        self.swap(i, -1)
        self.heap.pop()
        if i < len(self):
            self.siftup(i)
            self.siftdown(i)
        del self.indexof[val]


class DinnerPlates:
    def __init__(self, capacity: int):
        self.stacks = []
        self.heap = heap()
        self.capacity = capacity

    def push(self, val: int) -> None:
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        index = self.heap.pop() if len(self.heap) > 0 else -1
        self.stacks[index].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(-1)

    def popAtStack(self, index: int) -> int:
        index = index if index >= 0 else len(self.stacks) + index
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            self.heap.push(index)
            return self.stacks[index].pop()
        return -1


dp = DinnerPlates(1)

for method, arg in zip(methods, args):
    print(f"{method}({arg})")
    result = getattr(dp, method)(*arg)
    print(f"got: {result}")