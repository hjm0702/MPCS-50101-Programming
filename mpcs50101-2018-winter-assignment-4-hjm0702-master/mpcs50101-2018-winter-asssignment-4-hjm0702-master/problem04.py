def greated_common_divisor(a, b):
    # numbers = [a, b]
    # numbers.sort()
    # c = numbers[0]
    # d = numbers[1]
    if isinstance(a, int) == False or isinstance(b, int) == False:
        print "Input must be an integer."
    elif b == 0 or a == 0:
         return max(a,b)
    elif a == b:
        return a
    elif min(a,b) == 0 :
        return max(a,b)
    else:
        return greated_common_divisor(min(a,b), (max(a,b) % min(a,b)))

print greated_common_divisor(12, 9)
