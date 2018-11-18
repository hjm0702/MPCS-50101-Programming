'''
In Assignment 2, Problem 6
 - O(n) The algoritm has to compare each letter from the first half of a word to a letter from the other half.
 - https://github.com/uchicago-codes/mpcs50101-2018-winter-assignment-2-hjm0702/blob/master/pr06.py
'''
import re

def user_input():
    word = raw_input("Enter a word or phrase: ")
    return word

def valid_check():
    word = user_input()
    if re.search(r'\d', word):
        return ""
    elif word.isspace():
        return ""
    else:
        word_adj = []
        for i in word:
            if i.isalpha():
                word_adj.append(i.lower())
    return word_adj

final_word = valid_check()

def main(final_word):
    try:
        if len(final_word) == 1:
            return "This is a palindrome."
        elif len(final_word) == 2:
            if final_word[0] == final_word[-1]:
                return "This is a palindrome."
            return "This is not a palindrome."
        else:
            if final_word[0] == final_word[-1]:
                return main(final_word[1:-1])
            else:
                return "This is not a palindrome."
    except:
        return "Please input a word or pharse!"

print main(final_word)
