player_1_start_position = 10
player_2_start_position = 8

def deterministic_die():
    while True:
        i = 0
        while i < 100:
            i += 1
            yield i

def take_turn(current_score, current_pos, num_generator):
    total = sum([d for _, d in zip(range(3), num_generator)])

    current_pos = (current_pos + total) % 10
    current_score += current_pos + 1
    return current_score, current_pos

scores = [0, 0]
positions = [player_1_start_position-1, player_2_start_position-1]
die = deterministic_die()
throws = 0

while True:
    scores[0], positions[0] = take_turn(scores[0], positions[0], die)
    throws += 3
    if scores[0] >= 1000:
        break

    scores[1], positions[1] = take_turn(scores[1], positions[1], die)
    throws += 3
    if scores[1] >= 1000:
        break

print(scores)
print(positions)
print(throws)

print(min(scores) * throws)