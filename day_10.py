import data_getter

data = data_getter.get_data(10).splitlines()

x = 1
cycle = 1
key_cycles = [
    20, 60, 100, 140, 180, 220
]
values = []

def check(cycle, x):
    if cycle in key_cycles:
        values.append(x)

def generate_signal_strengths():
    result = []
    for i in range(len(key_cycles)):
        result.append(key_cycles[i] * values[i])
    return result

for line in data:
    line = line.split(' ')

    if line[0] == 'noop':
        cycle += 1
        check(cycle, x)
    elif line[0] == 'addx':
        cycle += 1
        check(cycle, x)

        cycle += 1
        x += int(line[1])
        check(cycle, x)

result = generate_signal_strengths()

print(f"The results are {result}")
print(f"The sum of all results is {sum(result)}")