import data_getter

data = data_getter.get_data(5).splitlines()

# First we need to get the stacks built

# You can't create 9 different lists like this-
#   this way creates 9 references to the same list (annoying)
# stacks = [[]] * 9

# This is how you create 9 different empty lists
stacks = [[] for n in range(9)]

for i in reversed(range(8)):
    for k in range(1,35,4):
        if data[i][k].isalpha():
            index = int((k-1)/4)
            stacks[index].extend(data[i][k])

instructions = data[10:]

for struct in instructions:
    struct = struct.split(' ')
    source = int(struct[3]) - 1
    dest = int(struct[5]) - 1
    amount = int(struct[1])

    temp = stacks[source][-amount:]
    del stacks[source][-amount:]
    stacks[dest].extend(temp)

print('Answer time!')

for stack in stacks:
    print(stack[-1])