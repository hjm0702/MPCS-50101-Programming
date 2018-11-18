pw = raw_input("Enter a password: ")
check = 0

if pw.isalpha() == False and pw.isdigit() == False and len(pw) >=12:
    for i in pw:
        if i == "!" or i == "@" or i == "#" or i == "$" or i == "%":
            for j in pw:
                if j.isupper() == True:
                    for k in pw:
                        if k.islower() == True:
                            check = check +1
                            break

if check ==1:
    print "This is a strong password."
else :
    print "This is not a strong password."
