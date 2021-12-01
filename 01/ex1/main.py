from itertools import tee

# Haven't updated to Python 3.10 yet, unfortunately.
# pairwise('ABCDEFG') --> AB BC CD DE EF FG
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



with open('input.txt', 'r') as open_file:
    numbers = [int(line.strip()) for line in open_file]

print(
    sum([a < b for a, b in pairwise(numbers)])
)