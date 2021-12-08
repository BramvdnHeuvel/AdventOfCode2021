from collections import Counter

lanternfish = Counter()

with open('input.txt', 'r') as open_file:
    jellies = ''.join([line for line in open_file])
    jellies = [int(j.strip()) for j in jellies.split(',')]

    lanternfish.update(jellies)

for _ in range(256):
    new_generation = Counter()

    for i in range(8):
        new_generation[i] = lanternfish[i+1]

    new_generation[6] += lanternfish[0]
    new_generation[8] += lanternfish[0]

    lanternfish = new_generation

print(lanternfish)
print(lanternfish.total())