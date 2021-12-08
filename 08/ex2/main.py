with open('input.txt', 'r') as open_file:
    digits = [line.strip() for line in open_file]

total = 0

for display in digits:
    values = display.split('|')[0].strip().split(' ')
    code   = display.split('|')[1].strip().split(' ')

    text_of_length = lambda n : [p for p in values if len(p)==n][0]

    mapping = {
        1: text_of_length(2), # 1 is the only number that uses two   segments
        4: text_of_length(4), # 4 is the only number that uses four  segments
        7: text_of_length(3), # 7 is the only number that uses three segments
        8: text_of_length(7), # 8 is the only number that uses seven segments
    }

    # Other numbers:
    # 5 segments: 2, 3, 5
    # 6 segments: 0, 6, 9

    intersection = lambda s1, s2 : ''.join([c for c in s1 if c in s2])

    # Number 6
    # 0 and 9 use both segments that 1 uses. Number 6 only uses 1.
    mapping[6] = [v for v in values if len(v) == 6 and len(intersection(v, mapping[1])) == 1][0]
    bottom_right = intersection(mapping[1], mapping[6])

    # Number 2
    # 3 and 5 use the bottom right segment. Number 2 doesn't.
    mapping[2] = [v for v in values if len(v) == 5 and bottom_right not in v][0]
    top_left = [c for c in mapping[6] if c not in mapping[1] and c not in mapping[2]][0]

    # Number 9
    # 4 is fully contained in 9. It is not in 0 or 6.
    mapping[9] = [v for v in values if len(v) == 6 and intersection(mapping[4], v) == mapping[4]][0]

    # Number 0
    # 0 is the last digit that uses 6 characters.
    mapping[0] = [v for v in values if len(v) == 6 and v not in [mapping[6], mapping[9]]][0]

    # Number 5
    # 2 and 3 don't use the top left segment. Number 3 does.
    mapping[5] = [v for v in values if len(v) == 5 and top_left in v][0]

    # Number 3
    # 3 is the last digit that uses 5 characters
    mapping[3] = [v for v in values if len(v) == 5 and v not in [mapping[2], mapping[5]]][0]

    result = ""
    for c in code:
        for num, digit in mapping.items():
            if set(digit) == set(c):
                result += str(num)
                break
    
    total += int(result)

print(total)