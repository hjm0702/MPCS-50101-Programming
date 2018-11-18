word = raw_input("Enter a word or phrase: ")
check = 0

if len(word)==1:
    print "This is a palindrome."
elif len(word) % 2 == 0:
    for i in range(len(word)/2):
        if word[i] == word[-1-i]:
            check = check + 1
elif len(word) % 2 != 0 :
    for i in range((len(word)-1)/2):
        if word[i] == word[-1-i]:
            check = check +1

if len(word) % 2 == 0:
    if check == len(word)/2:
        print "This is a palindrome."
    else:
        print "This is not a palindrome."
elif len(word) % 2 != 0 :
    if check == (len(word)-1)/2:
        print "This is a palindrome."
    else:
        print "This is not a palindrome."
