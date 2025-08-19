import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    choices = ["R", "P", "S"]
    return choices[len(opponent_history) % 3]
