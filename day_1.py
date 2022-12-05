import data_getter

data = data_getter.get_data(1).splitlines()

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