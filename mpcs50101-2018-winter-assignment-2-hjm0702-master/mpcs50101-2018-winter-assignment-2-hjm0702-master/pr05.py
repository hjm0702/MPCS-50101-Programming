num = raw_input("Enter a number: ")
check = 0

if num.isdigit() == True:
    if len(num) % 2 == 0:
        for i in range(len(num)/2):
            check = check + int(num[2*i]) - int(num[2*i+1])
    else:
        for i in range(len(num)/2):
            check = check - int(num[2*i+1]) + int(num[2*i+2])

if len(num) % 2 == 1:
    check = check + int(num[0])

if num.isdigit() == False:#
    print "Input is not an integer."
elif check % 11 == 0:
    print "This is divisible by 11."
elif check % 11 != 0:
    print "This is not divisible by 11."
