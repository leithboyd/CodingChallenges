# A = Rock, B = Paper, C = Scissors
WIN_SCORE = 6
LOSE_SCORE = 0
DRAW_SCORE = 3

second_player_wins = set([('A', 'B'), ('B', 'C'), ('C', 'A')])

shape_score = {
    'A': 1,
    'B': 2,
    'C': 3
}

def second_player_score(game):

    outcome_score = WIN_SCORE if game in second_player_wins else \
                    DRAW_SCORE if game[0] == game[1] else \
                    LOSE_SCORE

    return outcome_score + shape_score[game[1]]
    


strategy_guide = [(l[0], l[2]) for l in open('./day2/input.txt', 'r').read().splitlines()]

encoding =  {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}


total_score = sum(second_player_score((p1, encoding[p2])) for (p1, p2) in strategy_guide)

print(total_score)

