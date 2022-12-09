import data_getter

data = data_getter.get_data(9).splitlines()

head_pos = [0,0]
knots = []
for knot in range(9):
    knots.append([0,0])
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

def knot_move(knot):
    head = head_pos if knot == 0 else knots[knot-1]
    if abs(head[0] - knots[knot][0]) <= 1 and abs(head[1] - knots[knot][1]) <= 1:
        print('We good')
        return
    # Non-diagonal movement
    #   Y-axis movement
    elif head[0] == knots[knot][0]:
        if head[1] > knots[knot][1]:
            knots[knot][1] += 1
        else:
            knots[knot][1] -= 1
    #   X-axis movement
    elif head[1] == knots[knot][1]:
        if head[0] > knots[knot][0]:
            knots[knot][0] += 1
        else:
            knots[knot][0] -= 1
    # Diagonal time
    #   First, X-axis jump
    elif abs(head[0] - knots[knot][0]) > 1 and abs(head[1] - knots[knot][1]) <= 1:
        knots[knot][1] = head[1]
        if head[0] > knots[knot][0]:
            knots[knot][0] += 1
        else:
            knots[knot][0] -= 1
    #   Now Y-axis jump
    elif abs(head[1] - knots[knot][1]) > 1 and abs(head[0] - knots[knot][0]) <= 1:
        knots[knot][0] = head[0]
        if head[1] > knots[knot][1]:
            knots[knot][1] += 1
        else:
            knots[knot][1] -= 1
    # New diagonal movement time!
    elif head[0] > knots[knot][0]:
        if head[1] > knots[knot][1]:
            knots[knot][0] = head[0] - 1
            knots[knot][1] = head[1] - 1
        else:
            knots[knot][0] = head[0] - 1
            knots[knot][1] = head[1] + 1
    elif head[0] < knots[knot][0]:
        if head[1] > knots[knot][1]:
            knots[knot][0] = head[0] + 1
            knots[knot][1] = head[1] - 1
        else:
            knots[knot][0] = head[0] + 1
            knots[knot][1] = head[1] + 1


for ins in data:
    ins = ins.split(' ')
    for i in range(int(ins[1])):
        head_move(ins[0])
        for knot in range(9):
            knot_move(knot)
        visited.append(str(knots[8])) if str(knots[8]) not in visited else None

print(visited)
print(f"Number of visited coords is {len(visited)}")