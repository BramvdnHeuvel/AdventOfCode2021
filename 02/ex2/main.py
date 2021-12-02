import re

with open('input.txt', 'r') as open_file:
    instructions = [line.strip() for line in open_file]

horizontal, depth, aim = 0, 0, 0

for i in instructions:
    match = re.fullmatch(r'(\w+) (\d+)', i)
    direction, length = match[1], int(match[2])
    
    if direction == 'forward':
        horizontal += length
        depth      += aim * length
    elif direction == 'up':
        aim -= length
    else:
        aim += length

print(horizontal, depth)
print(horizontal * depth)