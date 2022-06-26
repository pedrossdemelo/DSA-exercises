# https://leetcode.com/problems/task-scheduler/

import heapq
from typing import Counter

# Time: O(nlogn) | Space: O(n)
def leastInterval(tasks, n):
    heap = [(-c, l) for l, c in Counter(tasks).most_common()]
    temp = []
    result = 0
    while heap:
        for _ in range(n + 1):
            if not heap:
                if not temp: break
                result += 1
                continue
            c, l = heapq.heappop(heap)
            result += 1
            c += 1
            if -c > 0:
                temp.append((c, l))
        while temp:
            heapq.heappush(heap, temp.pop())

    return result


tasks = ["A","A","A","B","B","B"]; n = 0
print(leastInterval(tasks, n))
