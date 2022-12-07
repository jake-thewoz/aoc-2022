import data_getter

data = data_getter.get_data(7).splitlines()

parent_dirs = []
dir_sizes = {}

for line in data:
    line = line.split(' ')
    print(f"Current line: {' '.join(line)}")

    if line[0] == '$':
        if line[1] == 'cd' and line[2] != '..':
            parent_dirs.append(line[2])
            dir_sizes['/'.join(parent_dirs)] = 0 
        elif line[1] == 'cd' and line[2] == '..':
            parent_dirs.pop()
            print(f"Back in dir {parent_dirs[-1]}")
    elif line[0].isnumeric():
        print(f"Adding the size of {line[1]} to every parent directory...")
        print(f"Parent directories {parent_dirs} will all have {line[0]} added to them...")
        temp_parent_dirs = parent_dirs.copy()
        while len(temp_parent_dirs) > 0:
            dir_sizes['/'.join(temp_parent_dirs)] += int(line[0])
            temp_parent_dirs.pop()

print(f"Size of all directories: {dir_sizes}")

print(f"Total space on device: {70000000}")
print(f"Total space used (/): {dir_sizes['/']}")
print(f"Current available space: {70000000 - dir_sizes['/']}")
print(f"Space needed for update: {30000000}")
print(f"Minimum space needing to be freed: {30000000 - (70000000 - dir_sizes['/'])}")

min_space = 30000000 - (70000000 - dir_sizes['/'])

suitable_dirs = { key:value for (key,value) in dir_sizes.items() if value >= min_space }

print(f"All suitable dirs: {suitable_dirs}")
print(f"Smallest of these: {min(suitable_dirs.values())}")