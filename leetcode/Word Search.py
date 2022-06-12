# https://leetcode.com/problems/word-search/


# n = rows, m = cols, 
# Time: O(n * m * 4^len(word))
def exist(board, word):
    ROWS, COLS = len(board), len(board[0])

    visited = set()

    def get_steps(coord):
        row, col = coord
        directions = (
            (row - 1, col), # up
            (row + 1, col), # down
            (row, col - 1), # left
            (row, col + 1), # right
        )
        return [
            (r, c)
            for r, c in directions
            if 0 <= r < ROWS
            and 0 <= c < COLS
            and (r, c) not in visited
            and board[r][c] == word[len(visited)]
        ]

    def dfs(coord):
        if len(visited) == len(word):
            raise Exception("found!")
        for n_coord in get_steps(coord):
            visited.add(n_coord)
            dfs(n_coord)
            visited.remove(n_coord)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word: return True
            if board[row][col] == word[0]:
                try:
                    visited.add((row, col))
                    dfs((row, col))
                    visited.remove((row, col))
                except Exception: return True

    return False

board = [["a","a"]]
word = "aaa"

print(exist(board, word))

