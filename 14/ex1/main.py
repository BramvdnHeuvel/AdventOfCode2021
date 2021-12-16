from itertools import pairwise
from collections import Counter
import re

with open('input.txt', 'r') as open_file:
    polymer = next(open_file).strip()
    next(open_file)

    pair_inserters = [
        re.findall(r'([A-Z])([A-Z]) -> ([A-Z])', line)[0]
        for line in open_file
    ]

connections = {}

for pair in pair_inserters:
    if pair[0] not in connections:
        connections[pair[0]] = {pair[1]: pair[2]}
    else:
        connections[pair[0]][pair[1]] = pair[2]

def polymizer(polymer, connections):
    for p1, p2 in pairwise(polymer):
        yield p1
        yield connections[p1][p2]
    else:
        yield p2

generator = polymer
for _ in range(10):
    generator = polymizer(generator, connections)

c = Counter(generator)
print(c)
print(c.most_common()[0][1] - c.most_common()[-1][1])
