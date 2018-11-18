#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(n):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    f = open(n, "r")
    files_raw = f.read()
    list_final = []
    list_notsorted = []
    dic = {}
    # dic_girl = {}
    reg1 = r'Popularity in (\d+)'
    reg2 = r'(\d+)</td><td>(\w+)</td><td>(\w+)'
    if re.search(reg1, files_raw):
        match1 = re.search(reg1, files_raw)
        list_final.append(match1.group(1))
        # print list_final

    if re.findall(reg2, files_raw):
        match2 = re.findall(reg2, files_raw)

    list_boy = []
    list_girl = []
    for i in match2:
        # print i[1]
        refer_boy = []
        refer_boy.append(i[1])
        refer_boy.append(i[0])
        # print refer_boy
        list_boy.append(refer_boy)
        refer_girl = []
        refer_girl.append(i[2])
        refer_girl.append(i[0])
        list_girl.append(refer_girl)
    # print list_notsorted

    for i in list_boy:
        if i[0] not in list_notsorted:
            list_notsorted.append(" ".join(i))

    for i in list_girl:
        if i[0] not in list_notsorted:
            list_notsorted.append(" ".join(i))

    list_notsorted.sort()
    for i in list_notsorted:
        list_final.append(i)

    return list_final

# print extract_names('baby1990.html')

    # list_notsorted.sort()

    # list_sorted = []
    # for i in list_notsorted:
    #     for j in list_notsorted:
    #         if i[0]==j[0] and i[1] != j[1]:
    #             if i[1] > j[1]:
    #                 list_sorted.append(j)
    #     list_sorted.append(i)
    #
    # for i in list_sorted:
    #     list_final.append(" ".join(i))
    # return list_final
    # for i in range(len(list_notsorted)-1):
    #     if list_notsorted[i][0] == list_notsorted[i+1][0]:
    #         # print list_notsorted[i][0], list_notsorted[i+1][0]
    #         if int(list_notsorted[i][1]) >= int(list_notsorted[i+1][1]):
    #             list_sorted.append(list_notsorted[i+1])
    #         else:
    #             list_sorted.append(list_notsorted[i])
    #     else:
    #         list_sorted.append(list_notsorted[i])
    # print list_sorted

    # print list_notsorted
    #         if i[0] == j[0] and i[1] != j[1]:
    #
    #             print i, j


        # dic[i[2]] = i[0]

    # for key, value in dic_boy.items() :
    #     for key_girl, value_girl in dic_girl.items() :
    #         if key_boy == key_girl:
    #             refer_both = []
    #             refer_both.append(key_boy)
    #             refer_both.append(min(value_boy, value_girl))
    #             list_notsorted.append(" ".join(refer_both))
    #         else:
    #             refer_boy = []
    #             refer_boy.append(key_boy)
    #             refer_boy.append(value_boy)
    #             list_notsorted.append(" ".join(refer_boy))
    #             refer_girl = []
    #             refer_girl.append(key_girl)
    #             refer_girl.append(value_girl)
    #             list_notsorted.append(" ".join(refer_girl)) # print refer

    # print list_notsorted
    #     # print match2.group(1), match2.group(2), match2.group(3)
    # return

# print extract_names('baby1990.html')

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]


    # if not args:
    #     print 'usage: [--summaryfile] file [file ...]'
    # sys.exit(1)
    #
    # # Notice the summary flag and remove it from args if it is present.
    # summary = False
    # if args[0] == '--summaryfile':
    #     summary = True
    #     del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
        # print args

    for filename in args:
        final = extract_names(filename)

    for i in final:
        print i



if __name__ == '__main__':
    main()
