# https://leetcode.com/problems/most-profit-assigning-work/

from typing import List

# n = len(profit|difficulty) | m = len(worker)
# Time: O(nlogn + mlogm) | Space: O(n)
def maxProfitAssignment(
    difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    jobs = sorted(zip(difficulty, profit)) # O(nlogn)
    totalprofit = i = best = 0
    for skill in sorted(worker):  # O(mlogm)
        while i < len(jobs) and skill >= jobs[i][0]:
            best = max(best, jobs[i][1])
            i += 1
        totalprofit += best
    return totalprofit



difficulty, profit, worker = (
    [68, 35, 52, 47, 86],
    [67, 17, 1, 81, 3],
    [92, 10, 85, 84, 82],
)

print(maxProfitAssignment(difficulty, profit, worker))
