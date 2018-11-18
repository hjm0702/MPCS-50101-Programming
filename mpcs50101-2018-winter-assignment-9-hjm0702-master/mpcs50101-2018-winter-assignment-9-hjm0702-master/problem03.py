''' Reduce: O(n) The fuction reduces an item by comparing two items in order.
    Linear: O(n) The function compares two items in order and swap the maximum value if needed.
    Binary: O(n^2) The function finds the maximum value with O(log(n)) time complexity
                   while it needs to sort items in ascending order before finding the value.

    In conclusion, Linear method is the fastest since it needs O(n) time with less swapping processes.
    Please refer to the attached, Problem03.png for the actual expeiments.
    '''

import random
import time
import math

randomlist = [random.randint(1,10000000) for i in range(1000)]

'''Reduce Function'''

def reducer(collection):
    max_number = reduce(lambda a,b: a if (a > b) else b , collection)
    return max_number

start_re = time.time()
print "Reduce: ", reducer(randomlist)
end_re = time.time()
print "Time:", end_re-start_re
print "================================="

'''Linear Search'''

def linear_search(collection):
    max_number = float("-inf")
    for i in range(len(collection)):
        if max_number < collection[i]:
            max_number = collection[i]
    return max_number

start_linear = time.time()
print "Linear:", linear_search(randomlist)
end_linear = time.time()
print "Time:", end_linear-start_linear
print "================================="


'''Binary Search'''

def binary_search(collection):
    sorted_list = sorted(randomlist)
    max_number = float("inf")
    left = 0
    right = len(sorted_list)-1
    while left <= right:
        mid = left + (right-left)/2
        if sorted_list[mid] < max_number:
            left = mid+1
    return sorted_list[mid]

start_binary = time.time()
print "Binary:", binary_search(randomlist)
end_binary = time.time()
print "Time:", end_binary-start_binary
