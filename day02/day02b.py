input_file = 'input.txt'

names = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
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
        outcome = names[text.split(' ')[1]]
        match = ('').join([opponent, '|', outcome])

        if (match == 'scissors|win') or (match == 'paper|lose') or (match == 'rock|draw'):
            player = "rock"
        elif (match == 'rock|win') or (match == 'scissors|lose') or (match == 'paper|draw'):
            player = "paper"
        else:
            player = "scissors"

        score = scoring[player] + scoring[outcome]
        # print('{} vs {} ({}, {})'.format(player, opponent, outcome, score))

        # increment score
        total_score += score

    print('Total score: {}'.format(total_score))
