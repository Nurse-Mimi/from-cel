from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You loose! " +computer+ " covers " +player)
        else:
            print("You win! " +player+ " smashes " +computer)
    elif player == "Paper":
        if computer == "scissors":
            print("You loose! " +computer+ " cuts " +player)
        else:
            print("You win! " +player+ " Covers " +computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose! " +computer+ " smashes " +player)
        else:
            print("You win! " +player+ " cuts " +computer)
    else:
        print("That is not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
