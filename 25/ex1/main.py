from cellular import CellularAutomaton

with open('input.txt') as open_file:
    herds = [line.strip() for line in open_file]

def check_step(lookup_func):
    value = lookup_func(0, 0)

    if value == '>':
        if lookup_func(1, 0) == '.':
            return 'v' if lookup_func(0, -1) == 'v' else '.'
        else:
            return '>'

    elif value == 'v':
        if lookup_func(0, 1) == '>' and lookup_func(1, 1) == '.':
            return '.'
        elif lookup_func(0, 1) == '.' and lookup_func(-1, 1) != '>':
            return '.'
        return 'v'

    else: # '.'
        if lookup_func(-1, 0) == '>':
            return '>'
        elif lookup_func(0, -1) == 'v':
            return 'v'
        else:
            return '.'

c = CellularAutomaton(
    next_state=check_step, default_value='.',
    neighbour_size=1,
    dimensions=[(0, len(herds[0])-1), (0, len(herds)-1)]
)

for y in range(len(herds)):
    for x in range(len(herds[y])):
        c.set_point(herds[y][x], x, y)

previous, current = None, c.values


c.run(iterations=100000)

