import word_resubmitted


def main(n):
    '''printing'''    

    dic = word_resubmitted.scoring(n)
    w = open('3_letter_words_sorted.txt', 'w')

    while len(dic) > 0:
        for key, value in dic.items():
            if value == max(dic.values()):
                w.write(str(key))
                w.write(' ')
                w.write(str(value))
                w.write('\n')
                print key, value
                del dic[key]

print main('3_letter_words.txt')
