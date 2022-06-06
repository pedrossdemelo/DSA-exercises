# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/



def longestIncreasingPath(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    mem_cache = [[None] * COLS for _ in range(ROWS)]

    def get_paths(row, col):
        directions = (
            (0,  1),  # right
            (0, -1),  # left
            (1,  0),  # down
            (-1, 0),  # up
        )

        return [
            (r + row, c + col)
            for r, c in directions
            if 0 <= r + row < ROWS and 0 <= c + col < COLS and matrix[r + row][c + col] > matrix[row][col]
        ]

    def dfs(row, col, path=0):
        nonlocal global_longest
        if mem_cache[row][col]:
            return mem_cache[row][col]

        valid_paths = get_paths(row, col)

        if not valid_paths:
            mem_cache[row][col] = 1
            return mem_cache[row][col]

        local_longest = 1
        for r, c in valid_paths:
            local_longest = max(local_longest, dfs(r, c, path + 1))
        mem_cache[row][col] = local_longest + 1
        global_longest = max(local_longest + 1, global_longest)
        return local_longest + 1

    global_longest = 0
    for row in range(ROWS):
        for col in range(COLS):
            dfs(row, col)

    return global_longest or 1


print(longestIncreasingPath([[1]]))
