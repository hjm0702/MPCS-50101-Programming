

'''Part A'''

def gcd_euclid(x,y):
    if isinstance(x, int) == False or isinstance(y, int) == False:
        return "Input must be an integer."
    elif x == 0 or y == 0:
        return max(x,y)
    elif x == y:
        return x
    else:
        return gcd_euclid(y, x % y)

print "Part A:", gcd_euclid(1000,99)

'''Part B'''
print
print "Part B:"

num_list = []

def gcd_repeated_substraction(x,y):
    num_list.append(x)
    num_list.append(y)

    if isinstance(x, int) == False or isinstance(y, int) == False:
        return "Input must be an integer."
    elif x == 0 and y == 0:
        print x, y, "// %d is the greatest common divisor of %d and %d" %(x, x, y)
    elif x == 0 or y == 0:
        print max(x, y), min(x, y), "// %d is the greatest common divisor of %d and %d" %(max(x,y), num_list[0], num_list[1])
    else:
        print max(x, y), min(x, y)
        return gcd_repeated_substraction(min(x, y), max(x, y)-min(x, y))


gcd_repeated_substraction(1000, 99)
