import random

computer_object = random.choice(["paper","rock","scissors"])

# check = raw_input("Would you like to play again? ")
ans = "Y"
while ans == "Y":
    choose = raw_input("Choose: ")
    if choose == "paper":
        if computer_object == "paper":
            print "The computer choose paper. Let's settle this."
        elif computer_object == "rock":
            print "The computer choose rock, you win!"
        elif computer_object == "scissors":
            print "Computer choose scissors, the computer wins :("
    elif choose == "rock":
        if computer_object == "rock":
            print "The computer choose rock. Let's settle this."
        elif computer_object == "scissors":
            print "The computer choose scissors, you win!"
        elif computer_object == "paper":
            print "Computer choose paper, the computer wins :("
    elif choose == "scissors":
        if computer_object == "scissors":
            print "The computer choose scissors. Let's settle this."
        elif computer_object == "paper":
            print "The computer choose paper, you win!"
        elif computer_object == "rock":
            print "Computer choose rock, the computer wins :("
    else:
        print "You must choose paper, rock or scissors."
    ans = raw_input('Do you want to play again? Y/N ')


# while not game_over :
#     game(choose)
    # if check == "n" or check == "N":
    #     game_over = True
