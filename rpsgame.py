import random


def pr_red(skk): print("\033[91m {}\033[00m" .format(skk))
def pr_light_purple(skk): print("\033[94m {}\033[00m" .format(skk))
def pr_purple(skk): print("\033[95m {}\033[00m" .format(skk))
def pr_cyan(skk): print("\033[96m {}\033[00m" .format(skk))


players_wins = 0
computer_wins = 0
continue_game = "yes"
while continue_game != "no":
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    player_move = input("Chose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Please try again...')
    computer_move = ""
    computer_random_int = random.randint(1, 3)
    if computer_random_int == 1:
        computer_move = rock
    elif computer_random_int == 2:
        computer_move = paper
    elif computer_random_int == 3:
        computer_move = scissors
    pr_red(f"The computer chose {computer_move}")
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        pr_light_purple("You win!")
        players_wins += 1
    elif player_move == computer_move:
        pr_light_purple("It's a draw!")
    else:
        pr_light_purple("You lose")
        computer_wins += 1
    pr_cyan("Type [yes] to play again or [no] to quit")
    continue_game = input()
pr_red(f'Result: player : computer -> {players_wins} : {computer_wins}')




