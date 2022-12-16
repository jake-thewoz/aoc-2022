import data_getter
import re

data = data_getter.get_data(15).splitlines()

[print(line) for line in data]

numbers = [re.findall(r'-?\d+', line) for line in data]

sensors = []
beacons = []
manhattan_distance = []

for line in numbers:
    sensors.append([int(line[0]), int(line[1])])
    beacons.append([int(line[2]), int(line[3])])
    manhattan_distance.append(abs(int(line[0]) - int(line[2])) + abs(int(line[1]) - int(line[3])))

print(sensors)
print(beacons)
print(manhattan_distance)

impossible = []
ROW = 2000000
# ROW = 10


for s in range(len(sensors)):
    sensor = sensors[s]
    reach = manhattan_distance[s]
    print(f'Calculating for sensor {sensor}, with reach {reach}')
    if (sensor[1] <= ROW and sensor[1] + reach >= ROW) \
        or (sensor[1] >= ROW and sensor[1] - reach <= ROW):
        spread = ((sensor[1] + reach) - ROW) if sensor[1] < ROW else (ROW - (sensor[1] - reach))
        print(f'Sensor is in range with a spread of {spread}')

        count = len(impossible)
        impossible.append(sensor[0])
        for i in range(1, spread+1):
            impossible.append(sensor[0] + i)
            impossible.append(sensor[0] - i)
        count -= len(impossible)
        print(f'{sensor} added {abs(count)} new entries to the list.')

print('Done finding the points.')
print(f'Before removing dups, the list has a size of {len(impossible)}')
print('Working on removing duplicates...')

s = set(impossible)
impossible = list(s)

# Now we're removing any beacons if they exist there
for beacon in beacons:
    if beacon[1] == ROW and beacon[0] in impossible:
        impossible.remove(beacon[0])

print(f'Done. There are {len(impossible)} points on row {ROW} where a beacon cannot be.')