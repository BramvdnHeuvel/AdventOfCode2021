from score_queue import ScoreQueue
from node import Node

with open('input.txt', 'r') as open_file:
# with open('15/ex1/input.txt', 'r') as open_file:
    route = [line.strip() for line in open_file]

DIMENSIONS = len(route)

def get_weight(coords):
    x, y = coords[0], coords[1]
    offset_x, offset_y = x // DIMENSIONS, y // DIMENSIONS

    x = x - DIMENSIONS*offset_x
    y = y - DIMENSIONS*offset_y
    offset = offset_x + offset_y
    
    score = int(route[x][y]) + offset
    if score > 9:
        score = score - 9
    return score

scores = [[float("inf") for _ in range(5*DIMENSIONS)] for _ in range(5*DIMENSIONS)]
scores[0][0] = 0

neighbouring_nodes = ScoreQueue()
neighbouring_nodes.put((0, 0))

while (coords := neighbouring_nodes.get()):
    x, y = coords[0], coords[1]

    score = scores[x][y]

    for dx, dy in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
        if x+dx<0 or y+dy<0 or x+dx>=5*DIMENSIONS or y+dy >= 5*DIMENSIONS:
            continue
        new_score = score + get_weight((x+dx, y+dy))
        current_score = scores[x+dx][y+dy]

        if new_score < current_score:
            scores[x+dx][y+dy] = new_score
            neighbouring_nodes.put((x+dx, y+dy))
        
    

print(scores[-1][-1])