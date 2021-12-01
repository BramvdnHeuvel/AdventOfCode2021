from itertools import pairwise


with open('input.txt', 'r') as open_file:
    numbers = [int(line.strip()) for line in open_file]

print(
    sum([a < b for a, b in pairwise(numbers)])
)
