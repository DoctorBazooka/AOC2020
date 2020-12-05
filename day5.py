def convert_col(string):
    return int(string.replace("F", "0").replace("B", "1"), 2)

def convert_row(string):
    return int(string.replace("L", "0").replace("R", "1"), 2)

val = 0
all_seats = set()
with open("day5_input.txt") as f:
    for line in f:
        seat = 8 * convert_col(line[:7]) + convert_row(line[7:])
        val = max(val, seat)
        all_seats.add(seat)

def find_seat(all_seats):
    for i in range(127 * 8):
        if i not in all_seats and {i+1, i-1} <= all_seats:
            return i
print(val)
print(find_seat(all_seats))