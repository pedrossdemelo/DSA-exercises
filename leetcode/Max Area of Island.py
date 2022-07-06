# https://leetcode.com/problems/max-area-of-island/

# Time: O(n) | Space: O(n)
from collections import deque


def maxAreaOfIsland(grid):  # DFS
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

        directions = (
            (row + 1, col),  # down
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row, col - 1),  # left
        )
        neighbours = [(r, c) for r, c in directions if 0 <= r < ROWS and 0 <= c < COLS]
        for neighbour in neighbours:
            visit(*neighbour)

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                visit(row, col)
                maxisland = max(maxisland, currisland)
                currisland = 0

    return maxisland


def maxAreaOfIsland(grid):  # BFS
    # 2 -> Visited territory
    # 1 -> Unvisited territory
    # 0 -> Water
    ROWS, COLS = len(grid), len(grid[0])
    maxisland = 0

    def bfs(row, col):
        queue = deque([(row, col)])
        currisland = 0

        while queue:
            row, col = queue.popleft()
            if grid[row][col] != 1:
                continue
            grid[row][col] = 2
            currisland += 1

            directions = (
                (row + 1, col),  # down
                (row - 1, col),  # up
                (row, col + 1),  # right
                (row, col - 1),  # left
            )

            neighbours = [
                (r, c)
                for r, c in directions
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
            ]

            for neighbour in neighbours:
                queue.append(neighbour)

        return currisland

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                maxisland = max(maxisland, bfs(row, col))

    return maxisland


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]

print(maxAreaOfIsland(grid))
