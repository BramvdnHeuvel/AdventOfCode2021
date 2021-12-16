from itertools import product

# with open('11/ex1/extra_1.txt', 'r') as open_file:
with open('input.txt', 'r') as open_file:
    octopus_grid = [[int(c) for c in line.strip()] for line in open_file]

def flash_nearby(grid, x, y):
    if x == y == 1:
        j = 1

    for dx, dy in zip([-1, -1, -1, 0, 0, 1, 1, 1], 
                      [-1, 0, 1, -1, 1, -1, 0, 1]):
        if x + dx < 0 or y + dy < 0:
            continue
        if x + dx > 9 or y + dy > 9:
            continue
        value = grid[x+dx][y+dy]
        if value == 10 or value == 0:
            continue

        grid[x+dx][y+dy] = value + 1
        if value + 1 == 10:
            grid = flash_nearby(grid, x + dx, y + dy)

    grid[x][y] = 0  # Make sure it doesn't accidentally flash twice
    return grid

i = 0
while True:
    i += 1
    new_grid = [[0 for _ in range(10)] for _ in range(10)]

    # Give all a slight bonus
    for x in range(10):
        for y in range(10):
            new_grid[x][y] = min(10, octopus_grid[x][y]+1)
        
    for x in range(10):
        for y in range(10):
            if new_grid[x][y] == 10:
                # The octopus flashes!
                new_grid = flash_nearby(new_grid, x, y)
            
    for x in range(10):
        for y in range(10):
            new_grid[x][y] = new_grid[x][y] % 10

    total_flashes = sum([len([o for o in row if o == 0]) for row in new_grid])
    
    if total_flashes == 100:
        print(f'After {i} generations, all octopuses flash simultaneously.')
        break
        
    octopus_grid = new_grid
