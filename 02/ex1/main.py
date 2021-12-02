import re

with open('input.txt', 'r') as open_file:
    instructions = [line.strip() for line in open_file]

horizontal, depth = 0, 0

for i in instructions:
    match = re.fullmatch(r'(\w+) (\d+)', i)
    direction, length = match[1], int(match[2])
    
    if direction == 'forward':
        horizontal += length
    elif direction == 'up':
        depth -= length
    else:
        depth += length

print(horizontal, depth)
print(horizontal * depth)