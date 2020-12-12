def load_board():
    with open("day11_input.txt") as f:
        return [[x for x in line.strip()] for line in f]

def neighbour_count_part1(old, row, col):
    neighbour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for x, y in neighbour_offsets:
        if 0 <= row + x < len(old) and 0 <= col + y < len(old[0]):
            if old[row + x][col + y] == "#":
                count += 1
    return count

def get_cell_part1(old, row, col):
    if old[row][col] == ".":
        return "."
    elif old[row][col] == "L":
        return "#" if neighbour_count_part1(old, row, col) == 0 else "L"
    else:
        return "L" if neighbour_count_part1(old, row, col) >= 4 else "#"

def get_next_board_part1(old):
    new = []
    for row in range(len(old)):
        new.append([])
        for col in range(len(old[0])):
            new[row].append(get_cell_part1(old, row, col))
    return new

def part1(initial_board):
    prev_board = []
    curr_board = initial_board
    while curr_board != prev_board:
        prev_board = curr_board
        curr_board = get_next_board_part1(curr_board)

    count = 0
    for row in curr_board:
        for seat in row:
            if seat == "#":
                count += 1
    return count


def raycast(old, row, col, dx, dy):
    row += dx
    col += dy
    while 0 <= row < len(old) and 0 <= col < len(old[0]):
        if old[row][col] in {"L", "#"}:
            return 1 if old[row][col] == "#" else 0
        row += dx
        col += dy
    return 0

def neighbour_count_part2(old, row, col):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        count += raycast(old, row, col, dx, dy)
    return count

def get_cell_part2(old, row, col):
    if old[row][col] == ".":
        return "."
    elif old[row][col] == "L":
        return "#" if neighbour_count_part2(old, row, col) == 0 else "L"
    else:
        return "L" if neighbour_count_part2(old, row, col) >= 5 else "#"

def get_next_board_part2(old):
    new = []
    for row in range(len(old)):
        new.append([])
        for col in range(len(old[0])):
            new[row].append(get_cell_part2(old, row, col))
    return new
    

def part2(initial_board):
    count = 0
    prev_board = []
    curr_board = initial_board
    while curr_board != prev_board:
        prev_board = curr_board
        curr_board = get_next_board_part2(curr_board)
        count += 1

    count = 0
    for row in curr_board:
        for seat in row:
            if seat == "#":
                count += 1
    return count

initial_board = load_board()

print(part1(initial_board))
print(part2(initial_board))