import data_getter

data = data_getter.get_data(9).splitlines()

head_pos = [0,0]
tail_pos = [0,0]
visited = []

def head_move(dr):
    if dr == 'R':
        head_pos[0] += 1
    elif dr == 'L':
        head_pos[0] -= 1
    elif dr == 'U':
        head_pos[1] += 1
    elif dr == 'D':
        head_pos[1] -= 1

def tail_move():
    if abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1:
        print('We good')
        return
    # Non-diagonal movement
    #   Y-axis movement
    elif head_pos[0] == tail_pos[0]:
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1
    #   X-axis movement
    elif head_pos[1] == tail_pos[1]:
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
    # Diagonal time
    #   First, X-axis jump
    elif abs(head_pos[0] - tail_pos[0]) > 1 and abs(head_pos[1] - tail_pos[1]) <= 1:
        tail_pos[1] = head_pos[1]
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
    #   Now Y-axis jump
    elif abs(head_pos[1] - tail_pos[1]) > 1 and abs(head_pos[0] - tail_pos[0]) <= 1:
        tail_pos[0] = head_pos[0]
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1

for ins in data:
    ins = ins.split(' ')
    for i in range(int(ins[1])):
        head_move(ins[0])
        print(head_pos)
        tail_move()
        print(tail_pos)
        visited.append(str(tail_pos)) if str(tail_pos) not in visited else None

print(visited)
print(f"Number of visited coords is {len(visited)}")