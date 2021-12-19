import re
from itertools import permutations

def reduce(value : str) -> str:
    """
        Reduce a snail number along the rules.
    """
    while (new_value := remove_nested_value(value)):
        value = new_value
        # print('after addition:', end='\t')
        # print(value)
    
    for m in re.finditer(r'\d+', value):
        if len(m.group(0)) >= 2:
            n = int(m.group(0))

            value = (
                value[:m.start()]           +
                str([n // 2, round(n / 2 + 0.1)]).replace(' ', '') +
                value[m.end():]
            )
            # print('after split:', end='\t')
            # print(value)

            return reduce(value)
    return value

def remove_nested_value(value):
    """
        Remove one tuple that is four layers deep
    """
    for m in re.finditer(r'\[\d+,\d+\]', value):
        if inside_four_pairs(value[:m.start()]):
            pair = [int(c) for c in m.group(0)[1:-1].split(',')]

            value = (
                increase_number(value[:m.start()], 'last', pair[0]) +
                str(0)                             +
                increase_number(value[m.end():], 'first', pair[1])
            )
            return value
    return False

def increase_number(value : str, pick : str, by : int):
    """
        Increase a value in a string.
        Use `pick` to indicate whether you'd like to
        change the `first` or the `last` integer.
    """
    i = 0 if pick == 'first' else -1
    try:
        n = [m for m in re.finditer(r'\d+', value)][i]
    except IndexError:
        return value
    else:
        new_number = int(n.group(0)) + by
        return value[:n.start()] + str(new_number) + value[n.end():]

def inside_four_pairs(left_string):
    """
        Check whether a value is in four pairs.
        This functions checks the string to the left.
    """
    return left_string.count('[') - left_string.count(']') >= 4

def magnitude(snail_number):
    def calculate_magnitude(m):
        pair = [int(c) for c in m.group(0)[1:-1].split(',')]
        prod = 3 * pair[0] + 2 * pair[1]
        return str(prod)

    new_number = re.sub(r'\[\d+,\d+\]', calculate_magnitude, snail_number)

    if snail_number != new_number:
        return magnitude(new_number)
    else:
        return int(new_number)

def main():
    with open('input.txt', 'r') as open_file:
        snail_numbers = [line.strip() for line in open_file]

    ms = []

    for a, b in permutations(snail_numbers, 2):
        ms.append(
            magnitude(
                reduce(
                    "[" + a + "," + b + "]"
                )
            )
        )
    
    print(max(ms))

if __name__ == '__main__':
    main()