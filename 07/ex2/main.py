from functools import lru_cache

with open('input.txt', 'r') as open_file:
    crabs = ''.join([line for line in open_file])
    crabs = [int(c) for c in crabs.split(',')]

DISTANCES, total = {}, 0

for i in range(max(crabs) - min(crabs) + 2):
    total += i
    DISTANCES[i] = total

def distance(crabs, medium):
    return sum([
        DISTANCES[abs(c - medium)] for c in crabs
    ])

print(min(
    [distance(crabs, i) for i in range(min(crabs), max(crabs)+1)]
))