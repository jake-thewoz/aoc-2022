import data_getter
import math

data = data_getter.get_data(8).splitlines()

height = len(data)
width = len(data[0])

# Data is a 99x99 square of trees

def find_score(row, column):
    north = 0
    if row > 0:
        for r in range(row-1, -1, -1):
            if int(data[r][column]) < int(data[row][column]):
                north += 1
            else:
                north += 1
                break
    east = 0
    if column < width - 1:
        for c in range(column+1, width, 1):
            if int(data[row][c]) < int(data[row][column]):
                east += 1
            else:
                east += 1
                break
    south = 0
    if row < height - 1:
        for r in range(row+1, height, 1):
            if int(data[r][column]) < int(data[row][column]):
                south += 1
            else:
                south += 1
                break
    west = 0
    if column > 0:
        for c in range(column-1, -1, -1):
            if int(data[row][c]) < int(data[row][column]):
                west += 1
            else:
                west += 1
                break

    return [north,east,south,west]

scenic_max = 0

for row in range(height):
    for column in range(width):
        scenic_score = find_score(row, column)
        print(f"Scenic score for [{row},{column}] is {scenic_score}")
        scenic_max = math.prod(scenic_score) if math.prod(scenic_score) > scenic_max else scenic_max

print(f"Scenic max is {scenic_max}")