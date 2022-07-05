# https://leetcode.com/problems/number-of-islands/

# The call stack can equal the amount of elements
# if and only if all elements are "1"
# Time: O(n) | Space: O(n)
def numIslands(grid):
    # 2 -> Visited territory
    # 1 -> Unvisited territory
    # 0 -> Water
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0

    def visit(row, col):
        if grid[row][col] != "1": # If it isn't unvisited territory, don't bother
            return
        grid[row][col] = "2" # Mark as visited

        paths = (
            (row + 1, col), # down
            (row - 1, col), # up
            (row, col + 1), # right
            (row, col - 1), # left
        )
        neighbours = [(r,c) for r,c in paths if 0 <= r < ROWS and 0 <= c < COLS]
        for neighbour in neighbours:
            visit(*neighbour)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                visit(row, col)
                islands += 1

    return islands

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]

print(numIslands(grid))