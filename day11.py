def load_board():
    with open("day11_input.txt") as f:
        return [[x for x in line.strip()] for line in f]

def neighbour_count(old, row, col):
    neighbour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for x, y in neighbour_offsets:
        if 0 <= row + x < len(old) and 0 <= col + y < len(old[0]):
            if old[row + x][col + y] == "#":
                count += 1
    return count

def get_cell(old, row, col):
    if old[row][col] == ".":
        return "."
    elif old[row][col] == "L":
        return "#" if neighbour_count(old, row, col) == 0 else "L"
    else:
        return "L" if neighbour_count(old, row, col) >= 4 else "#"

def get_next_board(old):
    new = []
    for row in range(len(old)):
        new.append([])
        for col in range(len(old[0])):
            new[row].append(get_cell(old, row, col))
    return new
    
prev_board = []
curr_board = load_board()
while curr_board != prev_board:
    prev_board = curr_board
    curr_board = get_next_board(curr_board)

count = 0
for row in curr_board:
    for seat in row:
        if seat == "#":
            count += 1
print(count)