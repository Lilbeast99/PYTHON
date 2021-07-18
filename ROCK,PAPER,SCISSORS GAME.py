import random
print("> > > ROCK PAPER SCISSORS < < <")
print("================================")
wins = 0
losses = 0
draws = 0

while True:
    print("\n%s Wins, %s Losses, %s draws" % (wins, losses, draws))
    # PLAYER'S CHOICE
    playermove = input("\nEnter your move\n(r)ock\n(p)aper\n(s)cissors\n>> ")
    if playermove == 'r':
        print("\nPLAYER CHOOSES ROCK...")
    elif playermove == 'p':
        print("\nPLAYER CHOOSES PAPER...")
    elif playermove == 's':
        print("\nPLAYER CHOOSES SCISSORS...")
    elif playermove == 'q':
        quit()
    else:
        print("Invalid Choice")

    # COMPUTER'S CHOICE
    rand = random.randint(1, 3)
    computermove = ''
    if rand == 1:
        computermove = 'r'
        print("COMPUTER CHOOSES ROCK")
    elif rand == 2:
        computermove = 'p'
        print("COMPUTER CHOOSES PAPER")
    elif rand == 3:
        computermove = 's'
        print("COMPUTER CHOOSES SCISSORS")

    # After evaluating computer's choice
    if playermove == computermove:
        print("It is a draw")
        draws += 1
    elif playermove == 'r' and computermove == 's':
        print("You win !")
        wins += 1
    elif playermove == 'p' and computermove == 'r':
        print("You win !")
        wins += 1
    elif playermove == 's' and computermove == 'p':
        print("You win !")
        wins += 1
    elif playermove == 'r' and computermove == 'p':
        print("You Loose !")
        losses += 1
    elif playermove == 'p' and computermove == 's':
        print("You Loose !")
        losses += 1
    elif playermove == 's' and computermove == 'r':
        print("You Loose !")
        losses += 1
