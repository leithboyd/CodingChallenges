ROCK='A'
PAPER='B'
SCISSORS='C'

LOSE='X'
DRAW='Y'
WIN='Z'

WIN_SCORE = 6
LOSE_SCORE = 0
DRAW_SCORE = 3

shapes = [ROCK, PAPER, SCISSORS]

second_player_wins = set([
    (ROCK, PAPER), 
    (PAPER, SCISSORS), 
    (SCISSORS, ROCK)
])

shape_score = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

def second_player_outcome_and_score(game):
    return (WIN, WIN_SCORE) if game in second_player_wins else \
           (DRAW, DRAW_SCORE) if game[0] == game[1] else \
           (LOSE, LOSE_SCORE)

strategy_entry_score = {}

for p1 in shapes:
    for p2 in shapes:
        game = (p1, p2)
        outcome, outcome_score = second_player_outcome_and_score(game)
        strategy_entry_score[(p1, outcome)] = outcome_score + shape_score[p2]

strategy_guide = [(l[0], l[2]) for l in open('./day2/input.txt', 'r').read().splitlines()]

total_score = sum(strategy_entry_score[entry] for entry in strategy_guide)

print(total_score)