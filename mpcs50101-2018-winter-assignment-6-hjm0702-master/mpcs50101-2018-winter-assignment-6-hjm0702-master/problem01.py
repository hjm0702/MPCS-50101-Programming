import itertools
import re

'''still creating codes but this is what I build so far :( '''


class InputValidator:
    '''validate input into a 7-letter format'''

    # def __str__(self):
    #     pass

def userinput():
    return ("Enter the each letter in your rack:")

def input_handling(letters):
    letters = userinput()
    letters_sorted = []
    reg1 = r'\d'
    reg3 = r'^\w,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*'
    reg4 = r'[~`!@\#$%^&*()-+\[\]\{\}|:;\"\'\.<>/?=_]'
    reg5 = r'\s'
    match = re.search(reg1, letters)
    if re.search(reg1, letters):
        return 'You must enter a letter, not a number.'
    elif re.search(reg4, letters):
        return "You must enter a letter, not a non-alphabet"
    elif re.search(reg3, letters):
        list1 = []
        for i in letters:
            if re.search(r'\w', i):
                list1.append(i)
        upper = []
        for i in list1:
            upper.append(i.upper())
    if len(upper) <= 7:
        return upper
    else:
        return "You can enter at most 7 letters."

# word = InputValidator()
# word.one = 'a'
# word.two = 'b'
# word.three = 'c'
# word.four = 'd'
# word.five = 'e'
# word.six = 'f'
# word.seven = 'g'

print input_handling(letters)

class WordGenerator:
    '''find possible combination of words by comparing the word list'''

def openfile(rawfile):
    '''open a text file'''
    open_file = open(rawfile)
    refer = open_file.read().split()
    return refer

def find(words):
    '''find possible words based on input'''
    list_allowed = []
    for word in refer:
        count = 0
        for char in word:
            if char in input_handling(letters):
                count = count + 1
            if count == len(word):
                list_allowed.append(word)
                count = 0
                # print count
    return list_allowed

tile_score = {"a": 1, "c": 3,
              "b": 3, "e": 1,
              "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}


class WordValidator:
    '''sort words by score'''

def calculation(letters):
    final_dic = {}
    for word in allowed(letters):
        total = 0
        for char in word:
            total = total + tile_score[char.lower()]
        final_dic[word] = total
    return final_dic

def sorting(letters):
    k = calculation(letters)
    # list_sorted = []
    # print k.get
    k_sorted = sorted(k, key=k.get, reverse=True)
    # print type(k_sorted)
    for r in k_sorted:
        print r, k[r]

print sorting(letters)
