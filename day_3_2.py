import data_getter
import os

if (os.path.exists("data_day_3.txt")):
    with open("data_day_3.txt", "r") as f:
        data = f.read()
else:
    data = data_getter.get_data(3)
    with open("data_day_3.txt", "r") as f:
        data = f.read()

data = data.splitlines()

print(data)

misplaced_badges = []

for i in range(0, len(data), 3):
    rucksack = data[i]
    for item in rucksack:
        if item in data[i+1] and item in data[i+2]:
            misplaced_badges.append(item)
            break

print(misplaced_badges)

ord_badges = []

for item in misplaced_badges:
    if item.isupper():
        ord_badges.append(ord(item) - 38)
    else:
        ord_badges.append(ord(item) - 96)

print(f'The sum of all priority badges is {sum(ord_badges)}.')