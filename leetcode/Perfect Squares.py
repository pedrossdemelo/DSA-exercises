# https://leetcode.com/problems/perfect-square/

import sys


def numSquares(n):
    sys.setrecursionlimit(10000)
    memo, squares = {1: 1}, [1]
    c_rt, c_sqrt = 1, 1
    while True:
        c_rt += 1
        c_sqrt = c_rt ** 2
        if c_sqrt > n: break
        if c_sqrt == n: return 1
        squares.append(c_sqrt)
        memo[c_sqrt] = 1

    def dfs(n):
        if n not in memo:
            min_sqrs = float("inf")
            for sq in reversed(squares):
                if sq > n: continue
                if min_sqrs == 2: break
                min_sqrs = min(min_sqrs, 1 + dfs(n - sq))
            memo[n] = min_sqrs

        return memo[n]

    return dfs(n)

print(numSquares(3428))
