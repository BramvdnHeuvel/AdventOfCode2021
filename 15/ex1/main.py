
with open('input.txt', 'r') as open_file:
# with open('15/ex1/input.txt', 'r') as open_file:
    route = [line.strip() for line in open_file]

def get_weight(coords):
    x, y = coords[0], coords[1]
    return int(route[x][y])

scores = [[0 for _ in range(100)] for _ in range(100)]

for x in reversed(range(100)):
    for y in reversed(range(100)):
        total = get_weight((x, y))

        if x < 99 and y < 99:
            total += min(
                scores[x+1][y],
                scores[x][y+1]
            )
        elif x < 99:
            total += scores[x+1][y]
        elif y < 99:
            total += scores[x][y+1]
        
        scores[x][y] = total

print(scores[0][0] - get_weight((0, 0)))
