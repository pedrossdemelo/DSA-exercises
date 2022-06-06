# https://leetcode.com/problems/minimum-path-sum/


def minPathSum(grid):
    ROWS, COLS = len(grid), len(grid[0])

    for row in range(ROWS - 1, -1, -1):
        for col in range(COLS - 1, -1, -1):
            if row == ROWS - 1 and col == COLS - 1:
                continue
            down = grid[row + 1][col] if row + 1 < ROWS else float("inf")
            right = grid[row][col + 1] if col + 1 < COLS else float("inf")
            best_path = min(down, right)
            grid[row][col] += best_path 

    return grid[0][0]


test_grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(test_grid))
