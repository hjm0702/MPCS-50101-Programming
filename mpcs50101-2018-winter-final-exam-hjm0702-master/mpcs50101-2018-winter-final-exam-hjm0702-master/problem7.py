# Problem 7
#
#
# A. Construct a program that prompts a user for word and determines if that
# word is a valid play in a Scrabble match.  Implement a linear search algorithm
# to detect if the word is valid by comparing it to the [list of allowed Scrabble words](scrabble_list.txt).
#
# Time your function and return it as part of the results.
#
# The program flow should be similar to this:
# % python problem3.py
# What is the word? qi
#
# Valid! (Found in 0.2 seconds)


import time

def finder(word):
    f = open('scrabble_list.txt')
    refer = f.read().split()


    found = False
    for i in refer:
        if i == word.upper():
            found == True
            return "Valid!"

    if found == False:
        return "Invalid!"
#
if __name__ == "__main__":
    word = raw_input("Please input a word.: ")
    start = time.time()
    a = finder(word)
    end = time.time()
    print a, "(Found in %.2f seconds)" %(end-start)


# B. Faced with this large unsorted list, would it be more efficient to sort the
# list first and then perform a binary search, or to just use a linear search?
# Explain your answer in terms of algorithm complexity.

I would say using a linear search is more efficient since it shows O(n) time complextity.
Sorting the list first requires O(n^2) time complexity it cannot offset the time saving by a binary search. 


# C. Since our list of Scrabble words will not change very much over time, it
# may be possible to consider the size as constant.  If this is the case, how
# would this change your answer in B.

Still same answer. Even though the size of the list is constant, sorting the list requires O(n^2) time complexity.
