

with open('input.txt', 'r') as open_file:
    cave_system = [line.strip() for line in open_file]

def count_paths(dic, current_path = ['start']):
    current_position = current_path[-1]
    if current_position == 'end':
        return 1

    next_steps = dic[current_position]

    next_steps = [
        option for option in next_steps 
        if option == option.upper() or option not in current_path
    ]

    return sum([count_paths(dic, current_path + [option]) for option in next_steps])

paths = {}

for line in cave_system:
    node_a, node_b = line.split('-')[0], line.split('-')[1]
    
    for _ in range(2):
        if node_a not in paths:
            paths[node_a] = [node_b]
        else:
            paths[node_a].append(node_b)
        
        node_a, node_b = node_b, node_a
    
print(count_paths(paths, ['start']))