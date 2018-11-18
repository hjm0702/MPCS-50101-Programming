def max_of_three(a,b,c):
    d = [a,b,c]
    d.sort()
    print d
    return d[-1]

print max_of_three(100,2,17)
