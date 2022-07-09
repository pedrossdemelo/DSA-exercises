# https://leetcode.com/problems/island-perimeter/

# Time: O(n) | Space: O(1)
def islandPerimeter(grid):
    ROWS, COLS = len(grid), len(grid[0])
    result = 0

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                result += 4
                if row > 0 and grid[row-1][col]: result -= 2 # If territory up
                if col > 0 and grid[row][col-1]: result -= 2 # If territory left
    return result


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

print(islandPerimeter(grid))
