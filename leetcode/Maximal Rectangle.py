# https://leetcode.com/problems/maximal-rectangle/

# n = rows, m = cols
# Time: O(n * m) | Space: O(m)
def maximalRectangle(matrix):
    ROWS, COLS, largest = len(matrix), len(matrix[0]), 0
    row_below, right = [[]] * COLS, []
    for row in range(ROWS - 1, -1, -1):
        right.clear()
        for col in range(COLS -1, -1, -1):
            if matrix[row][col] == '0':
                right.clear()
                row_below[col].clear()
                continue
            best_ends = set()
            if not row_below[col] and not right:
                best_ends.add((row, col))

            be_rb, be_s = (0, 0), 0
            for r, c in row_below[col]:
                if c > col:
                    if any(be[1] >= c for be in right):
                        if r + c < be_s:
                            continue
                        be_rb, be_s = (r, c), r + c
                    else:
                        if r + col < be_s:
                            continue
                        be_rb, be_s = (r, col), r + col
                if c == col:
                    if r + c < be_s:
                        continue
                    be_rb, be_s = (r, c), r + c
            if be_s > 0:
                best_ends.add(be_rb)

            be_r, be_s = (0, 0), 0
            for r, c in right:
                if r > row:
                    if any(be[0] >= r for be in row_below[col]):
                        if r + c < be_s:
                            continue
                        be_r, be_s = (r, c), r + c
                    else:
                        if row + c < be_s:
                            continue
                        be_r, be_s = (row, c), row + c
                if r == row:
                    if r + c < be_s:
                        continue
                    be_r, be_s = (r, c), r + c
            if be_s > 0:
                best_ends.add(be_r)

            for r, c in best_ends:
                largest = max(largest, (1 + r - row) * (1 + c - col))

            right = list(best_ends)
            row_below[col] = list(best_ends)

    return largest

matrix = [["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]
print(maximalRectangle(matrix))