with open('input.txt', 'r') as open_file:
    crabs = ''.join([line for line in open_file])
    crabs = [int(c) for c in crabs.split(',')]

def distance(crabs, medium):
    return sum([abs(c - medium) for c in crabs])

print(min(
    [distance(crabs, i) for i in range(min(crabs), max(crabs)+1)]
))