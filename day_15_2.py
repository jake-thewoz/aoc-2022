import data_getter
import re

data = data_getter.get_data(15).splitlines()

numbers = [re.findall(r'-?\d+', line) for line in data]

sensors = []
beacons = []
manhattan_distance = []

for line in numbers:
    sensors.append([int(line[0]), int(line[1])])
    beacons.append([int(line[2]), int(line[3])])
    manhattan_distance.append(abs(int(line[0]) - int(line[2])) + abs(int(line[1]) - int(line[3])))

impossible = set()
# ROW = 21
ROW = 4000001

# For part two, we'll use the same idea from part one
# We'll just apply it row-by-row, until we find a space in our desired range
#   that isn't impossible

for i in range(ROW):
    print(f"---Row {i}---")
    for s in range(len(sensors)):
        sensor = sensors[s]
        reach = manhattan_distance[s]

        # print(f'Checking for sensor {sensor}, with reach {reach}...')

        if (sensor[1] <= i and sensor[1] + reach >= i) \
            or (sensor[1] >= i and sensor[1] - reach <= i):

            spread = ((sensor[1] + reach) - i) if sensor[1] < i else (i - (sensor[1] - reach))

            # print(f'Hit: Applying sensor {sensor}, with spread {spread}')

            # count = len(impossible)

            impossible.add(sensor[0])
            impossible |= set(map(lambda k: sensor[0] + k, range(1, spread+1)))
            impossible |= set(map(lambda k: sensor[0] - k, range(1, spread+1)))
        
    if len(set(range(ROW)) - impossible):
        diff = list(set(range(ROW)) - set(impossible))[0]
        answer = [diff, i]
        print(f"Got the answer! It's {answer}")
        break
    else:
        impossible.clear()

print(f"The tuning frequency of the distress beacon is {(answer[0] * 4000000) + answer[1]}")