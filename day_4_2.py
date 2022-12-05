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
    pair = {}
    pair['a_start'] = int(item[0])
    pair['a_end'] = int(item[1][0])
    pair['b_start'] = int(item[1][1])
    pair['b_end'] = int(item[2])
    new_data.append(pair)
data = new_data

count = 0
for pair in data:
    if pair['a_start'] <= pair['b_start'] and pair['a_end'] >= pair['b_start']:
        count += 1
        print(pair)
    elif pair['b_start'] <= pair['a_start'] and pair['b_end'] >= pair['a_start']:
        count += 1
        print(pair)
    elif pair['a_end'] >= pair['b_end'] and pair['a_start'] <= pair['b_end']:
        count += 1
        print(pair)
    elif pair['b_end'] >= pair['a_end'] and pair['b_start'] <= pair['a_end']:
        count += 1
        print(pair)


print(f'The total pairs where one is contained in the other is {count}.')