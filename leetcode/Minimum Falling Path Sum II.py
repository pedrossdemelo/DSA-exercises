# https://leetcode.com/problems/minimum-falling-path-sum-ii

def getLowestIndexes(row):
    first = second = float("inf")
    i1 = i2 = -1
    for i, value in enumerate(row):
        if value <= first:
            second, i2 = first, i1
            first, i1 = value, i
        elif value <= second:
            second, i2 = value, i
    return (i1, i2)


def minFallingPathSum(grid):
    SIZE = len(grid)

    if SIZE == 1:
        return grid[0][0]

    row_below = grid[-1]
    curr_row = None
    for row in range(SIZE - 2, -1, -1):
        curr_row = [None] * SIZE
        lowest_below_i, second_lowest_below_i = getLowestIndexes(row_below)
        for col in range(SIZE - 1, -1, -1):
            curr_row[col] = grid[row][col] + (
                row_below[lowest_below_i]
                if col != lowest_below_i
                else row_below[second_lowest_below_i]
            )
        row_below = curr_row
    return min(curr_row)



print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))