
def apply_mask(num, mask):
    ret = num
    for idx, bit in enumerate(reversed(mask)):
        if bit == "X":
            continue

        bit_val = 2 ** idx
        if bit == "1" and num & bit_val == 0:
            ret += bit_val
        elif bit == "0" and num & bit_val != 0:
            ret -= bit_val
    return ret

def parse_mem_line(line):
    key, val = line.split(" = ")
    return int(key[4:-1]), int(val)

def part1(lines):
    mem = {}
    mask = "X" * 36
    for line in lines:
        line = line.strip()
        if line.startswith("mem"):
            key, val = parse_mem_line(line)
            mem[key] = apply_mask(val, mask)
        elif line.startswith("mask"):
            mask = line.split(" = ")[1]
    
    return sum(mem.values())

with open("day14_input.txt") as f:
    lines = f.readlines()

print(part1(lines))