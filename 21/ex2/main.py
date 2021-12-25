player_1_start_position = 10
player_2_start_position = 8

from collections import Counter

def take_turn(current_scores, player):
    new_scores = Counter()
    changed_anything = False

    for item, amount in current_scores.items():
        score_1, score_2, pos_1, pos_2 = item

        if score_1 >= 21 or score_2 >= 21:
            new_scores[(score_1, score_2, pos_1, pos_2)] += amount
            continue
        changed_anything = True

        if player == 1:
            for die_1 in range(1, 3+1):
                for die_2 in range(1, 3+1):
                    for die_3 in range(1, 3+1):
                        new_pos = (pos_1 + die_1 + die_2 + die_3) % 10
                        new_scores[(score_1+new_pos+1, score_2, new_pos, pos_2)] += amount
        else:
            for die_1 in range(1, 3+1):
                for die_2 in range(1, 3+1):
                    for die_3 in range(1, 3+1):
                        new_pos = (pos_2 + die_1 + die_2 + die_3) % 10
                        new_scores[(score_1, score_2+new_pos+1, pos_1, new_pos)] += amount

    return new_scores, changed_anything

scores = Counter()
scores[(0, 0, player_1_start_position-1, player_2_start_position-1)] = 1

while True:
    scores, c = take_turn(scores, 1)
    if not c:
        break
    if len(scores) == 0:
        i = 0

    scores, c = take_turn(scores, 2)
    if not c:
        break
    if len(scores) == 0:
        i = 0

# Once all games are complete, count the wins
wins = [0, 0]
print(len(scores))

for outcome, amount in scores.items():
    if outcome[0] >= 21:
        wins[0] += amount
    if outcome[1] >= 21:
        wins[1] += amount

print(wins)
print(max(wins))
