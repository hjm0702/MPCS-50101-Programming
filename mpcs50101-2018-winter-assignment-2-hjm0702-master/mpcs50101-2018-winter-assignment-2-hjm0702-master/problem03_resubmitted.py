input = raw_input("Password?")

def length_check(n):
    check1 = False
    blank = 0
    for i in n:
        if i == " ":
            blank = blank + 1
    if len(n)-blank >= 12:
        check1 = True
    return check1

def number(n):
    check2 = False
    for i in n:
        if i.isdigit():
            check2 = True
    return check2

def letter(n):
    check3 = False
    for i in n:
        if i.isalpha():
            check3 = True
    return check3

def special_letter(n):
    check4 = False
    for i in n:
        if i in '!@#$%':
            check4 = True
    return check4

def capital(n):
    check5 = False
    for i in n:
        if i.isupper():
            check5 = True
    return check5

def lower(n):
    check6 = False
    for i in n:
        if i.islower():
            check6 = True
    return check6

def password(n):
    check = 0
    if length_check(n) and number(n) and letter(n) and special_letter(n) and capital(n) and lower(n):
        check = check + 1
    if check == 1:
        return "This is strong"
    return "This is NOT strong"
    # if number(n):
    #     check = check + 1
    # if letter(n):
    #     check = check + 1
    # if special_letter(n):
    #     check = check + 1
    # if capital(n):
    #     check = check + 1
    # if lower(n):
    #     check = check +1

print password(input)
