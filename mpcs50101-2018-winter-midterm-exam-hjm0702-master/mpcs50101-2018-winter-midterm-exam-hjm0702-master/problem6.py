# Problem 6
#
# One of the best ways to improve as a Scrabble player is to memorize all the 2
# and 3 letter words allowed during game play.  It should be noted that many
# of the world's best Scrabble players believe it is a waste of time (and brain
# power) to learn the definitions.
#
# Given a list of all the 3 letter Scrabble words (3_letter_words.txt) write a
# program to sort the list by the highest scoring words.
#
# The file is in the following format, where the 3 letter word is following by
# a pipe, "|", and then the definition:
#
#  AAH | to exclaim in delight
#  AAL | East Indian shrub
#  AAS | [aa] (rough, cindery lava)
#
# You should create a module named `words` that will handle all the functions
# related to reading, scoring and sorting the list.
#
# When you run the program, it should import the words module to read in the 3
# letter word list, compute the score for each word, and sort the words by
# descending score (i.e. highest scoring words to lowest scoring words).  Print
# the words out in sorted order to a file named 3letter_words_sorted.txt.  You
# do not need to print out the definitions.
#


# Use the following dictionary to look up the point value for each word.  A
# words total point value is the sum of points of each letter.
tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

f = open('./3_letter_words.txt','r')

tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
'''
1. Make a three words list for referrence

2. split them into a three character

3. caclulate the numbers

4. make a dictionary of [(word: score)]

5. sort in decending way

6. print all of them

'''
# def calculate(n):
whole_words = f.read()
adj_words = whole_words.split('\n')

refer = []
for i in range(len(adj_words)):
    refer.append(adj_words[i][0:3])

# k = refer.remove("   ")
refer1 = refer[:-1]
score = []

for i in range(len(refer1)):
    for j in [0,1,2]:
        print tile_score[refer1[i][j].lower()]

print score
# #
# print calcuate("AAN")
#
# print tile_score["a"]
