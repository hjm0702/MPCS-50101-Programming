'''
1. Make a three words list for referrence

2. split them into a three character

3. caclulate the numbers

4. make a dictionary of [(word: score)]

5. sort in decending way

6. print all of them

'''

import os
tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}

def sorting(n):
    # f = open('./3_letter_words.txt','r')
    # print os.path.normpath(n)
    f = open(os.path.normpath(n))
    w = open('3_letter_words_sorted.txt', 'w')

    # def calculate(n):
    whole_words = f.read()
    adj_words = whole_words.split('\n')

    refer = []
    for i in range(len(adj_words)):
        refer.append(adj_words[i][0:3])

    # k = refer.remove("   ")
    refer.sort()
    refer1 = refer[2:]

    score = 0
    dic = {}
    for i in range(len(refer1)):
        for j in [0,1,2]:
            score = score + tile_score[refer1[i][j].lower()]

        dic[refer1[i]] = score
        score = score*0

    while len(dic) > 0:
        for key, value in dic.items():
            if value == max(dic.values()):
                w.write(str(key))
                w.write(' ')
                w.write(str(value))
                w.write('\n')
                print key, value
                del dic[key]

    # print dic

# print sorting('3_letter_words.txt')

# if __name__ == "__main__" :
#     main()

# print refer1
# print score
# #
# print calcuate("AAN")
#
# print tile_score["a"]
