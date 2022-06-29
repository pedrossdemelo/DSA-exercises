# https://leetcode.com/problems/most-profit-assigning-work/

from bisect import bisect
from itertools import islice
from typing import List

# n = len(profit|difficulty) | m = len(worker)
# Time: O(nlogn + mlogn) | Space: O(n)
def maxProfitAssignment(
    difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    n = len(profit)
    jobs = sorted(zip(difficulty, profit), key=lambda x: (x[0], -x[1]))  # O(nlogn)
    viablejobs = [jobs[0]]
    for diff, proft in islice(jobs, 1, n): # O(n)
        if viablejobs[-1][1] >= proft:
            continue
        viablejobs.append((diff, proft))
    del jobs
    totalprofit = 0
    for skill in worker:  # O(qlogn)
        bestjob = bisect(viablejobs, skill, key=lambda x: x[0]) - 1
        totalprofit += viablejobs[bestjob][1] if bestjob >= 0 else 0
    return totalprofit


difficulty, profit, worker = (
    [68, 35, 52, 47, 86],
    [67, 17, 1, 81, 3],
    [92, 10, 85, 84, 82],
)

print(maxProfitAssignment(difficulty, profit, worker))
