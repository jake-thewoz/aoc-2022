import data_getter

data = data_getter.get_data(8).splitlines()

height = len(data)
width = len(data[0])
print(f'height {height}')

# Data is a 99x99 square of trees
# So we know at least 98x4 (392) trees are visible around the edges

visible_count = 0

exterior_count = 0
interior_count = 0

# This will hold the max value in each direction (NESW)
max_in_directions = [0,0,0,0]

def find_maxes(row, column):
    north = 0
    if row > 0:
        for r in range(row-1, -1, -1):
            north = int(data[r][column]) if int(data[r][column]) > north else north
    east = 0
    if column < width - 1:
        for c in range(column+1, width, 1):
            east = int(data[row][c]) if int(data[row][c]) > east else east
    south = 0
    if row < height - 1:
        for r in range(row+1, height, 1):
            south = int(data[r][column]) if int(data[r][column]) > south else south
    west = 0
    if column > 0:
        for c in range(column-1, -1, -1):
            west = int(data[row][c]) if int(data[row][c]) > west else west

    return [north,east,south,west]

for row in range(height):
    for column in range(width):
        max_in_directions = find_maxes(row, column)
        if row == 0 or column == 0 or row == height-1 or column == width-1:
            # print(f"Visible: [{row},{column}] = {data[row][column]}")
            # print("Reason is border")
            visible_count += 1
            exterior_count += 1
        elif int(data[row][column]) > min(find_maxes(row,column)):
            print(f"Visible: [{row},{column}] = {data[row][column]}")
            print(f"Max in directions: {max_in_directions}")
            visible_count += 1
            interior_count += 1
        else:
            print(f"Not Visible: [{row},{column}] = {data[row][column]}")
            print(f"Max in directions: {max_in_directions}")

print(f'Number of visible trees: {visible_count}')
print(f'Exterior count: {exterior_count}')
print(f'Interior count: {interior_count}')