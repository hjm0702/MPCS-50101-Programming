f = open('./speech.txt', 'r')
refer = open('./common_words_100.txt', 'r')

def word_check(n):
    refer_list = refer.read().lower().strip().split()

# print refer_list

    punclist = [",",".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
    whole_words = f.read()

    for punc in punclist:
        whole_words = whole_words.replace(punc, "")

    list_split = whole_words.lower().strip().split()
    list_nosymbol = []

    list_split.sort()

    list_refined = []

    for i in list_split:
        if i not in refer_list:
            list_refined.append(i)
    # print list_r  efined

    dic = {}
    #
    for i in range(len(list_refined)):
        # dic[list_refined[i]] = list_refined.count[list_refined[i]]
        dic[list_refined[i]] = list_refined.count(list_refined[i])

    # print max(dic.values())
    dic20 = {}
    count = 0
    while count < 20:
        for key, value in dic.items():
        # print key, value
            if value == max(dic.values()):
                dic20[key] = value
                del dic[key]
                count = count + 1

    # Since I have two words showing up five times respectively, I ended up having 21 most-often-used words from the list.
    
    count1 = 0
    while count1 < 21:
        for key, value in dic20.items():
            if value == min(dic20.values()):
                print key, value
                del dic20[key]
                count1 = count1 + 1

             # dic20 = {}
    # for i in range(20):
    #     if dic.values() == max(dic.values()):
    #         print dic.item()



# print dic
print word_check(1)

'''
dic = {}
for i in range(len(split)):
    try :# for j in range(len(split_remove))
        split_remove.index(split[i])
    except ValueError:
        dic[split[i]] = split.count(split[i])

dic20 = {}
for i in range(0:20):
    if dic.values() == max(dic.values()):
        print dic.item()

# print list_split
# for i in list_split:
#     for j in list_split[i]:
#         if j in puclist:
#             j =


# print list_nosymbol
'''
