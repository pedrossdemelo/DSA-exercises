# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

field_tst = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def validate_battlefield(field):
    ROWS, COLS = len(field), len(field[0])
    ships_left = {1: 4, 2: 3, 3: 2, 4: 1}
    is_valid = True

    def visit(row, col):
        field[row][col] = field[row][col] + 2

    def is_valid_unvisited_coord(row, col):
        if (ROWS > row >= 0) and (COLS > col >= 0):
            return False if field[row][col] >= 2 else True
        return False # invalid coord

    def get_neighbours(row, col):
        possible_neighbours = (
            (row + 1, col, "down"),
            (row, col + 1, "right"),
            (row + 1, col - 1, "downleft"),
            (row + 1, col + 1, "downright"),
        )

        valid_neighbours = [
            (n_row, n_col, n_ori, field[n_row][n_col])
            for n_row, n_col, n_ori in possible_neighbours
            if is_valid_unvisited_coord(n_row, n_col)
        ]

        return valid_neighbours

    def find_extensions(row, col, ship_length=1, orientation=None):
        nonlocal ships_left, is_valid
        if not is_valid: return
        ship_extension = None
        neighbours = get_neighbours(row, col)

        for n_row, n_col, n_ori, n_val in neighbours:
            visit(n_row, n_col)

            if n_val == 1:
                if ship_extension:
                    is_valid = False
                    return
                ship_extension = (n_row, n_col, n_ori)

        if ship_extension:
            ext_row, ext_col, ext_ori = ship_extension

            last_orientation = (
                [orientation] if orientation else ("right", "down")
            )

            if ext_ori not in last_orientation or ship_length >= 4:
                is_valid = False
                return

            find_extensions(ext_row, ext_col, ship_length + 1, ext_ori)

        if not ship_extension:
            ships_left[ship_length] = ships_left[ship_length] - 1
            if ships_left[ship_length] < 0:
                is_valid = False

    for row in range(ROWS):
        if not is_valid:
            break
        for col in range(COLS):
            if not is_valid:
                break
            value = field[row][col]
            if value >= 2:
                continue
            visit(row, col)
            if value == 1:
                find_extensions(row, col)
                continue

    return all([left == 0 for left in ships_left.values()])


print(validate_battlefield(field_tst))
