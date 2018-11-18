'''
1. Make a three words list for referrence

2. split them into a three character

3. caclulate the numbers

4. make a dictionary of [(word: score)]

5. sort in decending way

6. print all of them

'''

import os

def sorting(n):

    '''reading files'''
    f = open(os.path.normpath(n))

    '''sorting'''
    whole_words = f.read()
    adj_words = whole_words.split('\n')

    refer = []
    for i in range(len(adj_words)):
        refer.append(adj_words[i][0:3])

    refer.sort()
    refer1 = refer[2:]

    return refer1

def scoring(n):
    '''scoring'''
    tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

    score = 0
    sort_words = sorting(n)
    dic = {}
    for i in range(len(sort_words)):
        for j in [0,1,2]:
            score = score + tile_score[sort_words[i][j].lower()]

        dic[sort_words[i]] = score
        score = score*0

    return dic

if __name__ == "__main__":
    main()
