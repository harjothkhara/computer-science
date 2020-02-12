import random


def process_choices(player_move, cpu_move):
    '''
    Assume that both moves are r, p or s
    '''
    wins = {"r": "s", "p": "r", "s": "p"}  # dictionary
    if player_move == cpu_move:
        # tie
        print("Tie")
        return 0
    elif wins[player_move] == cpu_move:
        # value of key
        # win
        print("Win!")
        return 1
    else:
        # lose
        print("You did not win")
        return -1


# REPL
wins = 0
losses = 0
ties = 0

choices = ["r", "p", "s"]

# LOOP
while True:
    # READ
    cmd = input("-> ")
    cpu_move = random.choice(choices)
    print(f"CPU picks {cpu_move}")
    # EVAL
    if cmd in choices:  # checking if we have a valid input
        results = process_choices(cmd, cpu_move)  # calling function
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        else:
            losses += 1
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        break
    else:
        print("I did not recognize that command")
# PRINT
    print(f"Score: {wins} / {losses} / {ties}")
