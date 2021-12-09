from itertools import product

with open('input.txt', 'r') as open_file:
    caves = [[int(c) for c in line.strip()] for line in open_file]

def find_lowest_points(caves):
    risk_level = 0

    for x in range(len(caves)):
        for y in range(len(caves[0])):
            risk = caves[x][y]

            for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                try:
                    if x + dx < 0 or y + dy < 0:
                        raise ValueError("Can't loop around the list")

                    close_risk = caves[x+dx][y+dy]
                except IndexError:
                    pass
                except ValueError:
                    pass
                else:
                    if close_risk <= risk:
                        break
            else:
                yield x, y

def find_higher_ups(caves, x, y):
    my_point = caves[x][y]

    for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        if x + dx < 0 or y + dy < 0:
            continue

        try:
            close_point = caves[x+dx][y+dy]
        except IndexError:
            pass
        else:
            if my_point < close_point < 9:
                yield x+dx, y+dy
                yield from find_higher_ups(caves, x+dx, y+dy)

basins = [len(set(find_higher_ups(caves, x, y))) + 1 for x, y in find_lowest_points(caves)]
basins.sort(reverse=True)

print(basins[0] * basins[1] * basins[2])