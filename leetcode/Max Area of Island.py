# https://leetcode.com/problems/max-area-of-island/

# Time: O(n) | Space: O(n)
def maxAreaOfIsland(grid):
    # 2 -> Visited territory
    # 1 -> Unvisited territory
    # 0 -> Water
    ROWS, COLS = len(grid), len(grid[0])
    maxisland = currisland = 0

    def visit(row, col):
        nonlocal currisland
        if grid[row][col] != 1:  # If it isn't unvisited territory, don't bother
            return
        grid[row][col] = 2  # Mark as visited
        currisland += 1

        paths = (
            (row + 1, col),  # down
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row, col - 1),  # left
        )
        neighbours = [(r, c) for r, c in paths if 0 <= r < ROWS and 0 <= c < COLS]
        for neighbour in neighbours:
            visit(*neighbour)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                visit(row, col)
                maxisland = max(maxisland, currisland)
                currisland = 0

    return maxisland


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(maxAreaOfIsland(grid))
