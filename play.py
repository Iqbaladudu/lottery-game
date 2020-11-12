from random import randint

# list of play options
options = ['Rock', 'Paper', 'Scissors']

# random play to computer
computer = options[randint(0, 2)]

# Player set = false
player = False

while player == False:
    # set player to True
    player = input('Rock, Paper, Scissors? ')
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Input the data carfully")
    # Player was set to true, but we want to be False so that loop always running
    player = False
    computer = options[randint(0,2)]