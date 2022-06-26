import heapq

# Time: O(nlogn) | Space: O(n)
def mincostToHireWorkers(quality, wage, k):
    workers = sorted((w / q, q) for q, w in zip(quality, wage))
    candidates = [-w[1] for w in workers[:k]]
    qualitysum = -sum(candidates)
    capital = qualitysum * workers[k - 1][0]
    heapq.heapify(candidates)
    for ratio, q in workers[k:]:
        high = -heapq.heapreplace(candidates, -q)
        if high != q:
            qualitysum += q - high
            capital = min(capital, qualitysum * ratio)
    return capital


quality = [1000, 1, 10, 10, 1]
wage = [100, 8, 2, 2, 7]
k = 3
print(mincostToHireWorkers(quality, wage, k))
