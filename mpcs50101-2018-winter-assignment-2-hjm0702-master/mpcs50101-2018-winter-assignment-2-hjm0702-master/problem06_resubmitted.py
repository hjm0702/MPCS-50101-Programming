word = raw_input("Enter a word or phrase: ")

def check(word):
    if len(word) == 1:
        return "This is a palindrome."
    elif len(word) == 2:
        if word[0] == word[-1]:
            return "This is a palindrome."
        return "This is not a palindrome."
    else:
        if word[0] == word[-1]:
            return check(word[1:-1])
        else:
            return "This is not a palindrome."

print check(word)
