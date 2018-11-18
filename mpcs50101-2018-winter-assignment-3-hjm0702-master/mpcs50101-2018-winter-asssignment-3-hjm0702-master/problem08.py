speech = open("./speech.txt", "r")
remove = open("./common_words_100.txt", "r")

whole_speech = speech.read()
whole_words = whole_speech.strip()
lowered = whole_words.lower()
punclist = [",",".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]

# List to remove
whole_remove = remove.read()
whole_words_remove = whole_remove.strip()
split_remove = whole_words_remove.split()


for punc in punclist:
    lowered = lowered.replace(punc, "")
# print lowered

split = lowered.split()
split.sort()
#
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

print dic
