# https://leetcode.com/problems/word-search/


# n = rows, m = cols,
# Time: O(n * m * 4^len(word)) | Space: O(1)
def exist(board, word):
    ROWS, COLS, LETTERS = len(board), len(board[0]), len(word)
    def dfs(r, c, i):
        if i == LETTERS: return True
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == word[i]:
            temp, board[r][c] = board[r][c], None
            if (   dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)):
                return True
            board[r][c] = temp
        return False
    for r in range(ROWS):
        if any(dfs(r, c, 0) for c in range(COLS)): return True
    return False

board = [["a", "a", "a"]]
word = "aaa"

print(exist(board, word))
