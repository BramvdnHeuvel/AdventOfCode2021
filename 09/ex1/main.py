from itertools import product

with open('input.txt', 'r') as open_file:
    caves = [[int(c) for c in line.strip()] for line in open_file]

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
            risk_level += risk + 1

print(risk_level)