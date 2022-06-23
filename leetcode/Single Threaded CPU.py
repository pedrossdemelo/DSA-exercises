# https://leetcode.com/problems/single-threaded-cpu/

import heapq


def getOrder(tasks):
    tasks = sorted(((*times, i) for i, times in enumerate(tasks)), reverse=True)
    heap = []
    time = 0
    order = []
    while heap or tasks:
        if not heap and tasks[-1][0] > time:
            qtime, ptime, i = tasks.pop()
            time = qtime
            heapq.heappush(heap, (ptime, i))
        while tasks and tasks[-1][0] <= time:
            _, ptime, i = tasks.pop()
            heapq.heappush(heap, (ptime, i))
        ptime, i = heapq.heappop(heap)
        time += ptime
        order.append(i)
    return order


instructions = [[5, 6], [9, 4], [3, 9], [3, 7], [1, 1], [6, 9], [9, 1]]

print(getOrder(instructions))
