import data_getter
import re

data = data_getter.get_data(15).splitlines()

numbers = [re.findall(r'-?\d+', line) for line in data]

sensors = []
beacons = []
manhattan_distance = []

for line in numbers:
    # manhattan distance is now the third int in the sensors list
    sensors.append([int(line[0]), int(line[1]), abs(int(line[0]) - int(line[2])) + abs(int(line[1]) - int(line[3]))])
    beacons.append([int(line[2]), int(line[3])])

impossible = set()
# ROW = 21
ROW = 4000001

# For part two, we'll use the same idea from part one
# We'll just apply it row-by-row, until we find a space in our desired range
#   that isn't impossible

# Turns out the solution for part one is far too slow for the data set.
# I've turned all the loops into vectorized functions

def find_impossible(sensor, spread):
    combine_positive = lambda k: sensor[0] + k
    combine_negative = lambda k: sensor[0] - k
    response = set(map(combine_positive, range(1, spread+1)))
    response |= set(map(combine_negative, range(1, spread+1)))
    response.add(sensor[0])
    return response

def find_spreads(sensor, row):
    return ((sensor[1] + sensor[2]) - row) if sensor[1] < row else (row - (sensor[1] - sensor[2]))

def create_sensor_list(row):
    return list(filter(lambda sensor: \
    (sensor[1] <= row and sensor[1] + sensor[2] >= row) \
    or (sensor[1] >= row and sensor[1] - sensor[2] <= row),
    sensors))

def generate_rows(sensor_list, row):
    return [row] * len(list(sensor_list))

def generate_spreads(sensor_list, rows):
    return list(map(find_spreads, sensor_list, rows))

def generate_impossibles(sensor_list, spreads):
    imp = set()
    imp.update(*map(find_impossible, sensor_list, spreads))
    # Doing this next AND step to try to save on memory
    imp &= set(range(ROW))
    return imp

rows = range(ROW)

r_sensor_lists = list(map(create_sensor_list, rows))
# print(r_sensor_lists)
r_rows = list(map(generate_rows, r_sensor_lists, rows))
# print(r_rows)
r_spreads = list(map(generate_spreads, r_sensor_lists, r_rows))
# print(r_spreads)
r_impossibles = list(map(generate_impossibles, r_sensor_lists, r_spreads))
# print(r_impossibles)

# Solution time!
answer = list(filter(lambda imp: len(set(range(ROW)) - imp), r_impossibles))
# print(answer)

y_answer = r_impossibles.index(answer[0])
x_answer = list(set(range(ROW)) - set(answer[0]))[0]

print(f"Got the answer! It's point {[x_answer, y_answer]}")
print(f"The tuning frequency of the distress beacon is {(x_answer * 4000000) + y_answer}")