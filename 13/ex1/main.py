import re

dots  = []
folds = []

with open('input.txt', 'r') as open_file:
    for line in open_file:
        if line.strip() == '':
            break
        
        dots.append(tuple(
            int(n) for n in line.strip().split(',')
        ))
    
    folds = [
        re.findall(r'fold along ([xy])=(\d+)', line.strip())[0]
        for line in open_file
    ]

for fold in folds:
    direction, coord = fold[0], int(fold[1])
    direction = 0 if direction == 'x' else 1

    new_dots = []
    for dot in dots:
        if dot[direction] < coord:
            new_dots.append(dot)
        else:
            dot = list(dot)
            dot[direction] = coord - abs(coord - dot[direction])
            new_dots.append(tuple(dot))
    
    dots = list(set(new_dots))
    dots.sort()

    break

print(len(dots))
print(dots)