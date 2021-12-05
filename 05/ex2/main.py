from collections import Counter
import re

with open('input.txt', 'r') as open_file:
    lines = ''.join([line for line in open_file])

lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', lines)

# Turn into integers
lines = [(int(line[0]), int(line[1]), int(line[2]), int(line[3])) for line in lines]

total = Counter()

def get_generator(first, last):
    def endlessly():
        while True:
            yield first

    if first == last:
        return endlessly()
    elif first > last:
        return reversed(range(last, first+1))
    else:
        return range(first, last+1)

for line in lines:
    for x, y in zip(get_generator(line[0], line[2]), get_generator(line[1], line[3])):
        position = (x, y)

        total[position] += 1

print(len([pos for pos, tot in total.items() if tot > 1]))