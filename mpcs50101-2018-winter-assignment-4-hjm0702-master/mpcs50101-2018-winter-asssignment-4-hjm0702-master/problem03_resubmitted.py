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
print first, '/'

def search(dirname):
    count = 0
    try :
        filenames = os.path.normpath(dirname)
            # filenames = os.listdir(dirname)
        # filenames.sort()
        # print dirname, '/'
        for filename in os.listdir(filenames):
            # full_filename = os.path.normpath(dirname)
            full_filename = os.path.join(dirname, filename)
            directory = os.path.dirname(filenames)
            # print full_filename
            if os.path.isdir(full_filename):
                # print os.path.splitdrive(directory)
                # print str(directory).count('e')
                # print str(directory).split('"\"')
                # print directory
                # print directory,">>>", filename,'/'
                print ' '*(len(directory)), filename,'/' #'  '*count,
                search(full_filename)
                # count = count +1
                # print count
            else:
                print ' '*(len(directory)), filename
            # count = 0
                # search(os.path.abspath(filename))
                # os.path.join(dirname, filename)

                # print os.path.join(dirname, filename)
            #     count = count + 1
            # else:
            #     print '  '*(count+1), filename
    except WindowsError:
        return "Can't find the directory you input"

# print search('c:\Users\Jungmin\Documents\GitHub\mpcs50101-2018-winter-assignment-4-hjm0702')
print search(first)
