import re

with open('input.txt', 'r') as open_file:
    bingo = ''.join([line for line in open_file])

bingo_cards = re.findall(r'(?:(?: *\d+ *){5}\n?){5}', bingo)

bingo_cards = [
    [
        [
            int(c) for c in row.split(' ') if c != ''
        ] for row in b.split('\n') if row != ''
    ] for b in bingo_cards
]

order = [int(n) for n in re.findall(r'(?:\d+,)+\d+', bingo)[0].split(',')]

def card_complete(card):
    if [True, True, True, True, True] in card:
        return True
    
    for i in range(5):
        for j in range(5):
            if card[j][i] == True:
                continue
            break
        else:
            return True
    return False

def bingo_card_score(bingo_card, order):
    cards_found = 0

    for number in order:
        cards_found += 1
        for i in range(5):
            try:
                place = bingo_card[i].index(number)
            except ValueError:
                pass
            else:
                bingo_card[i][place] = True
    
        if card_complete(bingo_card):
            return (
                -1 * cards_found,
                number * sum(
                    [sum([n for n in row if n != True]) for row in bingo_card]
                )
            )

values = [bingo_card_score(card, order) for card in bingo_cards]
values.sort()

print(values)