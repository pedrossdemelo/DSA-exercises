# https://leetcode.com/problems/island-perimeter/


def islandPerimeter(grid):
    ROWS, COLS = len(grid), len(grid[0])
    # 0 = Water | 1 = Land | 2 = Explored Land
    VISITED, result = 2, 0

    def perimeter_and_neighbours(row, col):
        DIRECTIONS = (
            (row - 1, col),  # up
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row, col + 1),  # right
        )
        neighbours = [
            (r, c)
            for r, c in DIRECTIONS
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != 0
        ]
        perimeter = 4 - len(neighbours)
        return perimeter, neighbours

    def dfs(row, col):
        nonlocal result
        grid[row][col] = VISITED
        perimeter, neighbours = perimeter_and_neighbours(row, col)
        result += perimeter
        for r, c in neighbours:
            if grid[r][c] is not VISITED:
                dfs(r, c)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                dfs(row, col)
                return result


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

print(islandPerimeter(grid))
