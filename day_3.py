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

misplaced_items = []

for rucksack in data:
    length = len(rucksack)
    first_compartment = rucksack[:int(length/2)]
    second_compartment = rucksack[int(length/2):]

    for item in first_compartment:
        if item in second_compartment:
            misplaced_items.append(item)
            break

ord_items = []

for item in misplaced_items:
    if item.isupper():
        ord_items.append(ord(item) - 38)
    else:
        ord_items.append(ord(item) - 96)

print(f'The sum of all priority items is {sum(ord_items)}.')