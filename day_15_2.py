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

def find_impossible(sensor, spread):
    combine_positive = lambda k: sensor[0] + k
    combine_negative = lambda k: sensor[0] - k
    response = set(map(combine_positive, range(1, spread+1)))
    response |= set(map(combine_negative, range(1, spread+1)))
    response.add(sensor[0])
    return response


def find_spreads(sensor, row):
    return ((sensor[1] + sensor[2]) - row) if sensor[1] < row else (row - (sensor[1] - sensor[2]))


for i in range(ROW):
    print(f"---Row {i}---")

    sensor_list = list(filter(lambda sensor: \
        (sensor[1] <= i and sensor[1] + sensor[2] >= i) \
        or (sensor[1] >= i and sensor[1] - sensor[2] <= i),
        sensors))
    
    rows = [i] * len(list(sensor_list))
    spreads = list(map(find_spreads, sensor_list, rows))
    impossible.update(*map(find_impossible, sensor_list, spreads))

    # print(list(sensor_list))
    # print(list(spreads))
    # print((impossible))

    if len(set(range(ROW)) - impossible):
        diff = list(set(range(ROW)) - set(impossible))[0]
        answer = [diff, i]
        print(f"Got the answer! It's {answer}")
        break
    else:
        impossible.clear()

print(f"The tuning frequency of the distress beacon is {(answer[0] * 4000000) + answer[1]}")