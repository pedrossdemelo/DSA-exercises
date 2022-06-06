def uniquePathsWithObstacles(obstacleGrid):
    ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
    row_below = [0] * (COLS - 1) + [1]

    right = 0
    for row in range(ROWS - 1, -1, -1):
        right = 0
        for col in range(COLS - 1, -1, -1):
            if obstacleGrid[row][col] == 1:
                row_below[col] = right = 0
                continue
            right += row_below[col]
            row_below[col] = right

    return right

print(uniquePathsWithObstacles([[0,0,0,0],[0,1,1,1],[0,0,1,0]]))