# https://leetcode.com/problems/unique-paths-iii/

def uniquePathsIII(grid):
    ROWS_COUNT, COLS_COUNT = len(grid), len(grid[0])

    start = end = None
    walkable_count = 0

    for row in range(ROWS_COUNT):
        for col in range(COLS_COUNT):
            match grid[row][col]:
                case 0:
                    walkable_count += 1
                case 1:
                    start = (row, col)
                case 2:
                    end = (row, col)

    possible_paths = 0

    visited = set()

    def is_walkable(coord):
        row, col = coord
        return 0 <= row < ROWS_COUNT and 0 <= col < COLS_COUNT and grid[row][col] != -1

    def dfs(coord):
        nonlocal possible_paths, visited
        if coord == end:
            possible_paths += 1 if len(visited) == walkable_count + 1 else 0
            return

        if coord not in visited:
            curr_row, curr_col = coord
            visited.add(coord)
            for row, col in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                new_coords = (curr_row + row, curr_col + col)
                if not is_walkable(new_coords):
                    continue
                dfs(new_coords)
            visited.remove(coord)

    dfs(start)

    return possible_paths


grid = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2],
]

print(uniquePathsIII(grid))
