import re

with open('input.txt', 'r') as open_file:
    values = next(open_file).strip()
    scores = re.findall(r'x=(\d+)..(\d+), y=(\-?\d+)..(\-?\d+)', values)[0]
    min_x, max_x = int(scores[0]), int(scores[1])
    min_y, max_y = int(scores[2]), int(scores[3])

def final_x_value(init_veloc_x):
    return sum(range(init_veloc_x+1))

def passes_through(init_veloc_x, init_veloc_y):
    x, y = 0, 0
    while y >= min_y:
        x += init_veloc_x
        y += init_veloc_y
        init_veloc_x = max(0, init_veloc_x-1)
        init_veloc_y += -1
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True
    return False

valid_x_velocities = [i for i in range(50) if min_x < final_x_value(i) < max_x]
print(valid_x_velocities)

for i in range(500):
    for init_x in valid_x_velocities:
        if passes_through(init_x, i):
            print((init_x, i, sum(range(i+1))))