import data_getter

data = data_getter.get_data(10).splitlines()

x = 1
cycle = 1
sprite = [1,2,3]

def check_newline(cycle):
    if cycle % 41 == 0:
        print('\n', end='')
        return 1
    return cycle

def draw(cycle, sprite):
    if cycle in sprite:
        print('#', end='')
    else:
        print('.', end='')

def noop():
    return

def addx(value):
    return x + value

for line in data:
    line = line.split(' ')

    if line[0] == 'noop':
        draw(cycle, sprite)
        noop()
        cycle += 1
        cycle = check_newline(cycle)
    else:
        draw(cycle, sprite)
        noop()
        cycle += 1
        cycle = check_newline(cycle)

        draw(cycle, sprite)
        x = addx(int(line[1]))
        sprite = [x, x+1, x+2]
        cycle += 1
        cycle = check_newline(cycle)