import data_getter

data = data_getter.get_data(2).splitlines()

print(data)

total_score = 0

guide = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1
    },
}

for game in data:
    score = 0

    if game[2] == 'X':
        score += 0
    elif game[2] == 'Y':
        score += 3
    elif game[2] == 'Z':
        score += 6

    score += guide[game[0]][game[2]]
    total_score += score

print(f'The total score using this new strategy would be {total_score}.')

