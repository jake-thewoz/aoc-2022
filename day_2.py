import data_getter

data = data_getter.get_data(2).splitlines()

print(data)

total_score = 0

guide = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    },
}

for game in data:
    score = 0

    if game[2] == 'X':
        score += 1
    elif game[2] == 'Y':
        score += 2
    elif game[2] == 'Z':
        score += 3

    score += guide[game[2]][game[0]]
    total_score += score

print(f'The total score using this strategy would be {total_score}.')