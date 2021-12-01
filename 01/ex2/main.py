from itertools import tee, pairwise

def threewise(iterable):
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


with open('input.txt', 'r') as open_file:
    numbers = [int(line.strip()) for line in open_file]

sums = [sum([a, b, c]) for a, b, c in threewise(numbers)]

print(
    sum([a < b for a, b in pairwise(sums)])
)
