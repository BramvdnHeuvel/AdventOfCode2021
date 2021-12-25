

with open('input.txt', 'r') as open_file:
    algorithm = next(open_file).strip()
    next(open_file)

    image_list = [line.strip() for line in open_file]

start_min, start_max = 0, max(len(image_list), len(image_list[0]))
image = set()
everything_else = '.'

for i in range(len(image_list)):
    for j in range(len(image_list[0])):
        if image_list[i][j] == '#':
            image.add((i, j))

mapping = {
    '.': '0',
    '#': '1'
}

# Count how many there are
print('Generation 0 count: ', end='')
if everything_else == '#':
    print(float('inf'))
else:
    print(len(image))

for generation in range(2):
    new_image = set()

    minimum = start_min - generation - 1
    maximum = start_max + generation + 1

    if everything_else == '.':
        new_else = algorithm[0]
    else:
        new_else = algorithm[511]

    for i in range(minimum, maximum + 1):
        for j in range(minimum, maximum + 1):
            number = ''
            # Determine neighbours
            for dx in range(-1, 1+1):
                for dy in range(-1, 1+1):
                    x = i + dx
                    y = j + dy

                    if minimum+1 <= x <= maximum-1 and minimum+1 <= y <= maximum-1:
                        value = '#' if (x, y) in image else '.'
                    else:
                        value = everything_else
                    
                    number += mapping[value]
                
            number = int(number, 2)
            if algorithm[number] == '#':
                new_image.add((i, j))
    image = new_image
    everything_else = new_else
    print(f'Generation {generation+1} count: ', end='')

    # Count how many there are
    if everything_else == '#':
        print('inf + ' + str(len(image)))
    else:
        print(len(image))