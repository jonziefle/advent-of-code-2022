input_file = 'input.txt'

names = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

scoring = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    "win": 6,
    "draw": 3,
    "lose": 0
}

with open(input_file) as input:
    lines = input.readlines()

    total_score = 0
    for line in lines:
        text = line.strip()

        opponent = names[text.split(' ')[0]]
        player = names[text.split(' ')[1]]
        match = ('').join([player, '|', opponent])

        if (match == 'rock|scissors') or (match == 'paper|rock') or (match == 'scissors|paper'):
            outcome = "win"
        elif (match == 'scissors|rock') or (match == 'paper|scissors') or (match == 'rock|paper'):
            outcome = "lose"
        else:
            outcome = "draw"

        score = scoring[player] + scoring[outcome]
        # print('{} vs {} ({}, {})'.format(player, opponent, outcome, score))

        # increment score
        total_score += score

    print('Total score: {}'.format(total_score))
