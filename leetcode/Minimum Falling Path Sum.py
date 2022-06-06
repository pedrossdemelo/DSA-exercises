# https://leetcode.com/problems/minimum-falling-path-sum/

def minFallingPathSum(matrix):
    SIZE = len(matrix)
    row_below = matrix[-1]
    curr_row = [None] * SIZE
    for row in range(SIZE - 2, -1, -1):
        curr_row = [None] * SIZE
        for col in range(SIZE - 1, -1, -1):
            curr_value = matrix[row][col]
            options = row_below[max(0,col-1):col+2]
            curr_row[col] = min(options) + curr_value
        row_below = curr_row
    return min(curr_row)

print(minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
