import data_getter
import os
import time

data = data_getter.get_data(14).splitlines()

# [print(line) for line in data]

rock_paths = []
all_x = []
all_y = []
visual = []

for line in data:
    endpoints = line.split(' -> ')
    rock_paths.append(endpoints)
    for point in endpoints:
        x_values = int(point.split(',')[0])
        y_values = int(point.split(',')[1])
        all_x.append(x_values)
        all_y.append(y_values)

# print(all_x)
# print(all_y)

vis_length = max(all_x) - min(all_x) + 3
vis_height = max(all_y) + 2
sand_drop = 500 - min(all_x) + 1

# print(vis_length)
# print(vis_height)

# Here we create our basic, empty visualization
for y in range(vis_height):
    visual.append([])
    if y == 0:
        for x in range(vis_length):
            if x == sand_drop:
                visual[-1].append('+')
            else:
                visual[-1].append('.')
    elif y == vis_height - 1:
        for x in range(vis_length):
            visual[-1].append('_')
    else:
        for x in range(vis_length):
            visual[-1].append('.')

# Here we convert the rock_paths into numbers that correspond on
#   our visualization
temp_rock_paths = []
for path in rock_paths:
    new_path = []
    for location in path:
        location = eval('[' + location + ']')
        location[0] = location[0] - min(all_x) + 1
        new_path.append(location)
    temp_rock_paths.append(new_path)
rock_paths = temp_rock_paths

# Now we paint on our rocks
for path in rock_paths:
    for i in range(1, len(path)):
        diff = [(path[i][0]-path[i-1][0]), (path[i][1]-path[i-1][1])]
        # print(diff)
        
        # First step is to paint the first rock, path[i-1]
        visual[path[i-1][1]][path[i-1][0]] = '#'
        # [print(' '.join(line)) for line in visual]
        while diff != [0,0]:
            # print(f'looping diff {diff}')
            # Lateral movement
            if diff[0] != 0:
                # print('lateral')
                if diff[0] > 0:
                    diff[0] -= 1
                    visual[path[i][1]][path[i-1][0]+diff[0]] = '#'
                else:
                    diff[0] += 1
                    # print(f"Check point {path[i-1]} and diff {diff}")
                    visual[path[i][1]][path[i-1][0]+diff[0]] = '#'
            # Vertical movement
            else:
                # print('vertical')
                if diff[1] > 0:
                    diff[1] -= 1
                    visual[path[i-1][1]+diff[1]][path[i][0]] = '#'
                    # print(diff)
                else:
                    diff[1] += 1
                    visual[path[i-1][1]+diff[1]][path[i][0]] = '#'
                    # print(diff)
            # [print(' '.join(line)) for line in visual]
        visual[path[i][1]][path[i][0]] = '#'
        # [print(' '.join(line)) for line in visual]


[print(' '.join(line)) for line in visual]

# Okay, whew. Now I'll work on the sand falling...

def find_next(current):
    # print(f"Evaluating {current}")
    if visual[current[1]+1][current[0]] == '_':
        print('Game over!')
        visual[current[1]+1][current[0]] = 'O'
        return [current[0],current[1]+1]
    elif visual[current[1]+1][current[0]] == '.':
        print('moving straight down')
        return [current[0], current[1]+1]
    elif visual[current[1]+1][current[0]] == 'o' or visual[current[1]+1][current[0]] == '#':
        if visual[current[1]+1][current[0]-1] == '.':
            print('moving down left')
            return [current[0]-1, current[1]+1]
        elif visual[current[1]+1][current[0]+1] == '.':
            print('moving down right')
            return [current[0]+1, current[1]+1]
        else:
            print('staying put')
            return current

game_on = True
counter = 0

while game_on:
    counter += 1


    # Here we make a sand kernel:

    current_pos = [sand_drop, 0]
    sand_falling = True

    while sand_falling:
        new_pos = find_next(current_pos)

        if visual[new_pos[1]][new_pos[0]] == 'O':
            sand_falling = False
            game_on = False
        elif new_pos == current_pos:
            sand_falling = False
            visual[new_pos[1]][new_pos[0]] = 'o'
        else:
            visual[new_pos[1]][new_pos[0]] = 'o'
            visual[current_pos[1]][current_pos[0]] = '.'
        
        current_pos = new_pos
            

        # time.sleep(.02)
        # os.system('cls')
        # [print(' '.join(line)) for line in visual]
    
print(f"{counter-1} grains of sand have stabilized.")