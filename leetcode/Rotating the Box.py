# https://leetcode.com/problems/rotating-the-box/


from typing import List

# Time: O(n) | Space: O(n)
def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    ROWS, COLS = len(box), len(box[0])

    for row in box:
        last_mass = 0
        for i, col in enumerate(row):
            if col == ".":  # col == empty space
                row[i], row[last_mass] = row[last_mass], row[i]
                last_mass += 1
            if col == "*":  # col == wall
                last_mass = i + 1

    return [[box[r][c] for r in range(ROWS)] for c in range(COLS)]


box = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", ".", "*", "#", "."],
]

rotated = [
    ["#", "#", "."],
    ["#", "#", "#"],
    ["*", "#", "#"],
    [".", "*", "*"],
    ["*", ".", "."],
    [".", ".", "#"],
]

print(rotateTheBox(box))
