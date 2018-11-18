import random

computer_object = random.choice(["paper", "rock", "scissors"])
def game(choice):
    again = True
    while again:
        print computer_object
        player_check = ["rock", "paper", "scissors"]
        computer_check = ["scissors", "rock", "paper"]

        choice = raw_input("Choose: ")
        if choice not in ["paper", "rock", "scissors"]:
            return 'You must choose paper, rock or scissors.'
        elif choice == computer_object:
            print 'The computer choose',computer_object,'. Lets settle this'
        elif player_check.index(choice) == computer_check.index(computer_object):
            print "You won"
        elif player_check.index(choice) == computer_check.index(computer_object) - 1:
            print "You lose"

        again_again = 1
        while again_again > 0:
            again_question = raw_input("Wanna play again?")
            if again_question in ["N", "n"]:
                again_again = 0
                again = False
            elif again_question not in ["Y", "y", "N", "n"]:
                print "Please input Y or N."
            elif again_question in ["Y", 'y']:
                again_again = 0

print game(1)
