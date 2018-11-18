def process_file(n):
    original_file = open(n, 'r')
    count = 0

    # b = original_file.read()
    # count = sum(1 for line in open(n))
    for i in open(n):
        count = count + 1

    sort = sorted(original_file.read().split(), key=str.lower)

    # return count
    # print original_file.read()
    # word = []

    return n, sort, count


print process_file('common_words_100.txt')
