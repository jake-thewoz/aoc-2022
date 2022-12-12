import data_getter

data = data_getter.get_data(12).splitlines()

# This one seems like a classic path-finding problem

# First I'll generate a list of 'unvisited' nodes
nodes = []
visual = []

for y in range(len(data)):
    visual.append([])
    for x in range(len(data[y])):
        visual[y].append('.')
        if data[y][x] == 'S':
            start_node = {
                'height': ord('a'),
                'coords': [x, y],
                'visited': False,
                'shortest_path': [],
                'distance': 0
            }
            nodes.append(start_node)
        elif data[y][x] == 'E':
            end_node = {
                'height': ord('z'),
                'coords': [x, y],
                'visited': False,
                'shortest_path': [],
                'distance': 0
            }
            nodes.append(end_node)
        else:
            new_node = {
                'height': ord(data[y][x]),
                'coords': [x, y],
                'visited': False,
                'shortest_path': [],
                'distance': 0
            }
            nodes.append(new_node)

def find_neighbors(node):
    neighbors = []
    neighbors.append(next((n for n in nodes if n['coords'][0] - 1 == node['coords'][0] and n['coords'][1] == node['coords'][1]), None))
    neighbors.append(next((n for n in nodes if n['coords'][0] + 1 == node['coords'][0] and n['coords'][1] == node['coords'][1]), None))
    neighbors.append(next((n for n in nodes if n['coords'][1] - 1 == node['coords'][1] and n['coords'][0] == node['coords'][0]), None))
    neighbors.append(next((n for n in nodes if n['coords'][1] + 1 == node['coords'][1] and n['coords'][0] == node['coords'][0]), None))
    neighbors = [n for n in neighbors if n is not None]
    neighbors = [n for n in neighbors if n['height'] - node['height'] <= 1]
    return neighbors

queue = []

queue.insert(0, start_node)

while queue: 
    current_node = queue.pop()
    current_node['visited'] = True
    visual[current_node['coords'][1]][current_node['coords'][0]] = '#'
    print(f"Processing node {current_node['coords']}")
    neighbors = find_neighbors(current_node)

    for neighbor in neighbors:
        if not neighbor['visited'] and neighbor not in queue:
            neighbor['distance'] += current_node['distance'] + 1
            queue.insert(0, neighbor)



print(end_node)

for line in visual:
    print(' '.join(line))