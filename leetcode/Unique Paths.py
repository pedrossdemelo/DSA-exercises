# https://leetcode.com/problems/unique-paths/

def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    row_below, right = [1] * n, 1
    for _ in range(m - 2, -1, -1):
        right = 1
        for col in range(n - 2, -1, -1):
            right += row_below[col]
            row_below[col] = right
    return right

print(uniquePaths(9,9))