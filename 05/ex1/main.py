from collections import Counter
import re

with open('input.txt', 'r') as open_file:
    lines = ''.join([line for line in open_file])

lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', lines)

# Turn into integers
lines = [(int(line[0]), int(line[1]), int(line[2]), int(line[3])) for line in lines]

# Only consider straight lines
lines = [line for line in lines if line[0] == line[2] or line[1] == line[3]]

total = Counter()

for line in lines:
    low_x, high_x = min(line[0], line[2]), max(line[0], line[2])
    low_y, high_y = min(line[1], line[3]), max(line[1], line[3])

    for x in range(low_x, high_x+1):
        for y in range(low_y, high_y+1):
            position = (x, y)

            total[position] += 1

print(len([pos for pos, tot in total.items() if tot > 1]))