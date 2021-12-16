from itertools import pairwise
from collections import Counter
import re

with open('input.txt', 'r') as open_file:
    polymer = next(open_file).strip()
    last_letter = polymer[-1]
    next(open_file)

    pair_inserters = [
        re.findall(r'([A-Z])([A-Z]) -> ([A-Z])', line)[0]
        for line in open_file
    ]

connections = {}

for pair in pair_inserters:
    connections[pair[0] + pair[1]] = (
        pair[0] + pair[2], pair[2] + pair[1]
    )

c = Counter([a+b for a, b in pairwise(polymer)])

for _ in range(40):
    new_c = Counter()

    for elem, value in c.items():
        for strain in connections[elem]:
            new_c[strain] += value

    c = new_c

final_c = Counter({last_letter: 1})

for elem, value in c.items():
    final_c[elem[0]] += value
c = final_c

print(c)
print(c.most_common()[0][1] - c.most_common()[-1][1])