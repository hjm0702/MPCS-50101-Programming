import random

f = open('common_words_100.txt', 'r')

entire_file = f.read()
answer = entire_file.split()[random.randint(0,100)]
# print answer


def hangman():
    sample = []
    play_again = True
    count = 5
    letters = ""

    while play_again:
        raw_letter = raw_input(">>> Guess a letter?")
        if raw_letter.isalpha():
            letter = raw_letter.lower()

        if len(letter) != 1:
            print "Please enter a single letter."
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print "Please enter a LETTER."
        else:
            if letter in answer:
                letters = letters + letter
                print letter, "is in the word",
                for char in answer:
                    if char in letters:
                        print char,
                    else:
                        print "_",
                print
                guessed_word = raw_input(">>> Try and guess the word.")
                if guessed_word == answer:
                    print "Congratulations!  The word was", answer
                    break
                print "That is not the word"
            else:
                print letter, "is not in the word."
                count = count - 1
                if count == 0:
                    print
                    again = raw_input("You lost. Would you play again? y or n")
                    if again == "Y" or again == "y":
                        print "Let's play again"
                        count = count + 5
                    elif again == "N" or again == "n":
                        break
                else:
                    print "You have", count, "guesses remaining."
                # print letter, "is in the word", " ".join(sample)
print hangman()
