# https://leetcode.com/problems/battleships-in-a-board/


# Time: O(n) | Space: O(1)
def countBattleships(board):
    ROWS, COLS = len(board), len(board[0])

    def nei(row, col):
        for r, c in ((row + 1, col), (row, col + 1)):
            if not 0 <= r < ROWS or not 0 <= c < COLS: continue
            if board[r][c] == "X":
                return (r, c)
        return None

    ships = 0
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                board[row][col] = "."
                ships += 1
                r, c = row, col
                while nei(r, c):
                    r, c = nei(r, c)
                    board[r][c] = "."
    return ships


board = [
    [".", "X", ".", ".", "X"],
    [".", "X", ".", ".", "X"],
    [".", ".", ".", ".", "X"],
    ["X", ".", "X", "X", "."],
    ["X", ".", ".", ".", "X"],
]

print(countBattleships(board))
