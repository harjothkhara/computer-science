import random

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
    if cmd == "r":
      # Do rock
        if cpu_move == "r":
            print("You Tie")
            ties += 1
        elif cpu_move == "p":
            print("You Lose")
            losses += 1
        elif cpu_move == "s":
            print("You Win!")
            wins += 1
    elif cmd == "p":
      # Do paper
        if cpu_move == "r":
            print("You Win!")
            wins += 1
        elif cpu_move == "p":
            print("You Tie")
            ties += 1
        elif cpu_move == "s":
            print("You Lose")
            losses += 1
    elif cmd == "s":
      # Do scissors
        if cpu_move == "r":
            print("You Lose")
            losses += 1
        elif cpu_move == "p":
            print("You Win!")
            wins += 1
        elif cpu_move == "s":
            print("You Tie")
            ties += 1
    elif cmd == "q":
      # Quit
        print("Goodbye!")
        break
    else:
        print("I did not recognize that command")
# PRINT
    print(f"Score: {wins} / {losses} / {ties}")
