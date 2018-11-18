'''python2'''

import random
from sys import argv
f = open('numbers.txt', 'w')

script, first = argv
n = first

# n = raw_input("Input: ")


def median(n):
    if len(n) ==1:
        return n[0]
    elif len(n) ==2:
        return (n[0]+n[1])/2.0
    else:
        n.sort()
        return median(n[1:-1])


def mean(n):
    mean = 0
    for i in range(len(n)):
        mean = mean + n[i]
    return mean/float(len(n))

def mode(n):
    lst = []
    for i in range(len(n)):
        lst.append(n.count(n[i]))
    m = max(lst)
    ml = [x for x in n if n.count(x) == m]
    mode = []
    for x in ml:
        if x not in mode:
            mode.append(x)
    if len(mode) > 1:
        return "No mode"
    else:
        return mode[0]

def variance(n):
    var = 0
    for i in n:
        var = var + (i-mean(n))**2
    return var/float(len(n))

def standard_deviation(n):
    return variance(n)**(0.5)

if __name__ == "__main__":
    def random_number(n):

        if n.isdigit() == False:
            return "Input must be an integer."
        elif n == '0' :
            return "The number must be a positive integer."
        else:
            numbers = []
            for x in range(int(n)):
                x = random.randint(0, 100)
                numbers.append(x)
                f.write(str(x))
                f.write("\n")

            # print numbers
            print "mean:", mean(numbers)
            print "median:", median(numbers)
            print "mode:", mode(numbers)
            print "variance:", variance(numbers)
            print "standard deviation:", standard_deviation(numbers)


    print random_number(n)
