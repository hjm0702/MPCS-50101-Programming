def max_of_three(a,b,c):
    d = 0
    if a > b:
        if a > c:
            d = a
        else:
            d = c
    elif b > c:
        d = b
    else:
        d = c
    print d

print max_of_three(15,1,3)
