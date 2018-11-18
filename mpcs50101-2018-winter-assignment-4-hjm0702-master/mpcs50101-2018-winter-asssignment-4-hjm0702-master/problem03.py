'''
We can use below module and fuction to list file names and subdirectories.

import os
os.walk()
'''

import sys
import os

script, first = sys.argv
#
# print "Argv: ", sys.argv
# print "First: ", first
#
# def walk_path():


def search(dirname):
    count = 0
    filenames = os.path.normpath(dirname)
    # filenames = os.listdir(dirname)
    # filenames.sort()
    for filename in os.listdir(filenames):
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            print '  '*count, filename,'/'
            # search(os.path.abspath(filename))
            # os.path.join(dirname, filename)

            # print os.path.join(dirname, filename)
            search(full_filename)
            count = count + 1
        else:
            print '  '*(count+1), filename

# print search('c:\Users\Jungmin\Documents\GitHub\mpcs50101-2018-winter-assignment-4-hjm0702')
print search(first)
'''
