# https://leetcode.com/problems/loud-and-rich/
from collections import defaultdict
from typing import List

# Time: O(n**2) | Space: O(n)
def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    richerthan = [[] for _ in range(n)]
    for rich, lessrich in richer:
        richerthan[lessrich].append(rich)
    answer = [None] * n

    def dfs(person):
        if answer[person] is None:
            answer[person] = person
            for rich in richerthan[person]:
                answer[person] = min(
                    answer[person], dfs(rich), key=lambda prsn: quiet[prsn]
                )
        return answer[person]

    for i in range(n):
        dfs(i)

    return answer


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
print(loudAndRich(richer, quiet))
