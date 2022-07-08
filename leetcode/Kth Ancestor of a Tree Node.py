# https://leetcode.com/submissions/detail/741849226/

import math
from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        logn = math.ceil(math.log2(n)) + 1
        self.logn = logn
        self.n = n

        # the ancestor for 1st, 2nd, 4th, ... , 2^(logn - 1)
        ancestor = [[-1 for _ in range(logn)] for _ in range(n)]

        # 1st ancestor (parent)
        for i in range(n):
            ancestor[i][0] = parent[i]

        # 2nd, 4th, ... , logn - 1 ancestors
        for exponent in range(1, logn):
            for i in range(n):
                if ancestor[i][exponent-1] != -1:
                    ancestor[i][exponent] = ancestor[ancestor[i][exponent-1]][exponent-1]

        self.ancestor = ancestor

    def getKthAncestor(self, node: int, k: int) -> int:
        for exponent in range(self.logn - 1, -1, -1):
            if k >= (2 ** exponent):
                node = self.ancestor[node][exponent]
                k -= 2 ** exponent

            if node == -1:
                return -1

        return node


methods, args = (
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"],
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
)

solution = TreeAncestor(*args[0])

for method, arg in zip(methods[1:], args[1:]):
    print(getattr(solution, method)(*arg))