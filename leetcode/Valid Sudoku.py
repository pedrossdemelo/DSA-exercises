# https://leetcode.com/problems/valid-sudoku/

def isValidSudoku(board):
    blocks = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]

    for row, rowArray in enumerate(board):
        for col, value in enumerate(rowArray):
            if value == ".":
                continue
            block = 3 * (row // 3) + col // 3
            if value in blocks[block] or value in rows[row] or value in cols[col]:
                return False
            blocks[block].add(value)
            cols[col].add(value)
            rows[row].add(value)

    return True


print(
    isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
