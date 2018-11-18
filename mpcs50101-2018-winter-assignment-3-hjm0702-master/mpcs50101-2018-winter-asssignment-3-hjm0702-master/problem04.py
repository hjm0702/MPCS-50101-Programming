filename = ""
number_of_lines = 0
sorted_items = []
# clean_items = []

def process_file(filename):
    filename = open('./common_words_100.txt', 'r')
    number_of_lines = 0
    for line in filename:
        number_of_lines = number_of_lines + 1
        sorted_items.append(line.strip( ))
    sorted_items.sort()
    # print sorted_items
    # print clean_items
    return filename, sorted_items, number_of_lines

print process_file(filename)
