import data_getter
import os

if (os.path.exists("data_day_1.txt")):
    with open("data_day_1.txt", "r") as f:
        data = f.read()
else:
    data = data_getter.get_data(1)
    with open("data_day_1.txt", "r") as f:
        data = f.read()

data = data.splitlines()

elves = []
counter = 0
for food in data:
    if food is '':
        elves.append(counter)
        counter = 0
    else:
        counter += int(food)

elves.append(counter)

print(elves)
print(f'The elf with the highest calories has {max(elves)}.')