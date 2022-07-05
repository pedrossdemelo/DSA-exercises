# https://leetcode.com/problems/surrounded-regions/

# Time: O(n) | Space: O(1)
def solve(board):
    ROWS, COLS = len(board), len(board[0])

    def getneighbours(row, col):
        paths = (
            (row - 1, col),  # up
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row, col + 1),  # right
        )
        return [
            (r, c)
            for r, c in paths
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O"
        ] 

    def visitneighbours(row, col):
        if board[row][col] != "O":
            return
        board[row][col] = "E"  # If "O" has a border neighbour, then mark it "E"scaped
        for neighbour in getneighbours(row, col):
            visitneighbours(*neighbour)

    # Visit only nodes with neighbours in the borders
    for row in range(ROWS):
        for col in range(0, COLS, COLS - 1 if 0 < row < ROWS - 1 else 1):
            visitneighbours(row, col)

    # Now that the "E"scaped nodes are marked, we can
    # return them to "O" and overwrite the unescaped "O"'s
    # to "X"
    for row in range(ROWS):
        for col in range(COLS):
            match board[row][col]:
                case "E":
                    board[row][col] = "O"
                case "O":
                    board[row][col] = "X"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

solve(board)
print(board)
