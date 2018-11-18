'''
1. Handle user input
# 2. Identify combination(XXXXXX)

3. Compare each alphabet of allowed list to given user input

4. Calculate score

5. Print words and scores
'''
import itertools
import re


letters = raw_input("> Enter the each letter in your rack"'\n')
''' check point
1. Zero Input
2. Alphabet or not?
3. Capital or lower?
4. comma or space?
5. irregular comma or space?
6. not same chracter
'''
def input_handling(letters):
    # reg = r'\w\W*\w\W*\w\W*\w\W*\w\W*\w\W*\w\W*'
    letters_sorted = []
    reg1 = r'\d' #valid
    # reg2 = r'\w{0,7}' #valid
    # reg3 = r'\w(,\w),'
    reg3 = r'^\w,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*\w*,*\s*'
    reg4 = r'[~`!@\#$%^&*()-+\[\]\{\}|:;\"\'\.<>/?=_]' #  ]'
    reg5 = r'\s'
    match = re.search(reg1, letters)
    if re.search(reg1, letters):
        # print 'You must enter a letter, not a number.'
        return 'You must enter a letter, not a number.'
    elif re.search(reg4, letters):
        return "You must enter a letter, not a non-alphabet"
    elif re.search(reg3, letters):

    # if letters. "":
    #     print "You should input at least one letter."
    # else:
    #
        list1 = []
        for i in letters:
            if re.search(r'\w', i):
                list1.append(i)
        # result = list1
        upper = []
        for i in list1:
            upper.append(i.upper())
    # print upper
    if len(upper) <= 7:
        # print "Finding results"
        return upper
    else:
        return "You can enter at most 7 letters."
    # return upper

print input_handling(letters)

# def ident(letters):
#     list_com = []
#     list_final = []
#     for i in range(len(letters)):
#         k = list(itertools.combinations(input_handling(letters),i+1))
#         for j in k:
#             list_com.append(j)
#     for i in list_com:
#         k = list(itertools.permutations(i))
#         for j in k:
#             list_final.append("".join(j))
#     return list_final
        # list_perm.append(list(itertools.combinations(input_handling(letters),i+1)))
    #     list_perm.append("".join(p))
    # return list_perm

def allowed(letters):
    f = open('scrabble_list.txt')
    refer = f.read().split()
    list_allowed = []

    # if refer[100][1] in input_handling(letters):
    #     print "Yes", refer[100]
    # print refer[100]

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
    # for i in refer:
    #
    # return input_handling(letters)
tile_score = {"a": 1, "c": 3,
              "b": 3, "e": 1,
              "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    # for i in ident(letters):
    #     if i.upper() in refer:
    #         list_allowed.append(i)
    # return list_allowed
    # for i in iden(letters) :
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
    # print k_sorted.items()

    # for key, value in k.items():
    #     if value == max(k.values()):
    #         list_temp = []
    #         list_temp.append(key)
    #         list_temp.append(str(value))
    #         list_sorted.append(" ".join(list_temp))
    #         print list  _sorted
    #         del k[value]
    #         sorting(k)
    # return list_sorted

print sorting(letters)
