import random

while True:
    choices= ["rock","paper","scissors"]

    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,paper or scissors : ").lower()

    if player == computer :

        print("player : ",player)
        print("computer : ",computer)
        print("Tie!")
    elif player == "rock":
        if computer=="paper":
            print("player : ",player)
            print("computer : ",computer)
            print("computer won!") 
        if computer=="scissors":
            print("player : ",player)
            print("computer : ",computer)
            print("player won!")
    elif player == "paper":
        if computer=="rock":
            print("player :",player)
            print("computer :",computer)
            print("player won!") 
        if computer=="scissors":
            print("player : ",player)
            print("computer : ",computer)
            print("computer won!")
    elif player == "scissors":
        if computer=="paper":
            print("player : ",player)
            print("computer : ",computer)
            print("player won!") 
        if computer=="rock":
            print("player : ",player)
            print("computer : ",computer)
            print("computer won!")

    play_again=input("Play again? (yes/no) : ").lower()
    if play_again != "yes":
        break

print("bye! loser")