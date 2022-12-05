import data_getter
import os

if (os.path.exists("data_day_4.txt")):
    with open("data_day_4.txt", "r") as f:
        data = f.read()
else:
    data = data_getter.get_data(4)
    with open("data_day_4.txt", "r") as f:
        data = f.read()

data = data.splitlines()

new_data = []
for item in data:
    item = item.split('-')
    item[1] = item[1].split(',')
    flat_dat = []
    # We need to convert to ints because string comparison is unreliable
    flat_dat.append(int(item[0]))
    flat_dat.append(int(item[1][0]))
    flat_dat.append(int(item[1][1]))
    flat_dat.append(int(item[2]))
    new_data.append(flat_dat)
data = new_data

count = 0
for pair in data:
    if (pair[0] <= pair[2]) and (pair[1] >= pair[3]):
        count += 1
    elif (pair[0] >= pair[2]) and (pair[1] <= pair[3]):
        count += 1

print(f'The total pairs where one is contained in the other is {count}.')