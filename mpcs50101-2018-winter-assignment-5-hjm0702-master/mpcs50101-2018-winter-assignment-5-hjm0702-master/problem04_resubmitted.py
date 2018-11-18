'''
1. Handle user input
# 2. Identify combination(XXXXXX)

3. Compare each alphabet of allowed list to given user input

4. Calculate score

5. Print words and scores
'''
import itertools
import re

''' check point
1. Zero Input
2. Alphabet or not?
3. Capital or lower?
4. comma or space?
5. irregular comma or space?
6. not same chracter
'''
def input_handling():
    letters = raw_input("> Enter the each letter in your rack"'\n')

    reg_true = r'[a-zA-Z]'
    reg_false1 = r'\d'
    reg_false2 = r'[^a-zA-Z,\s]'

    match = re.findall(reg_true, letters)
    match_final = []

    if re.search(reg_false1, letters):
        print "Please input only letters."
    elif re.search(reg_false2, letters):
        print "Please input only letters!"
    else:
        if len(match) > 7:
            print "Please input at most 7 letters."
        else:
            for char in match:
                match_final.append(char.upper())
            return match_final

def allowed():
    '''find valid words given the text file'''
    f = open('scrabble_list.txt')
    refer = f.read().split()
    list_allowed = []
    user_input = input_handling()

    try :
        for word in refer:
            count = 0
            for char in word:
                if char in user_input:
                    count = count + 1
                if count == len(word):
                    list_allowed.append(word)
                    count = 0
        return list_allowed
    except :
        return False

def calculation():
    '''calculate the scores of the validated words'''
    tile_score = {"a": 1, "c": 3,
    "b": 3, "e": 1,
    "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

    final_dic = {}
    try :
        for word in allowed():
            total = 0
            for char in word:
                total = total + tile_score[char.lower()]
            final_dic[word] = total
        return final_dic
    except:
        return False


def sorting():
    '''sorting the list by score'''
    k = calculation()
    try :
        k_sorted = sorted(k, key=k.get, reverse=True)
        for r in k_sorted:
            print r, k[r]
    except :
        return ""

print sorting()
