'''Think about how many operations (ie. comparing letters, keeping state of an index, storage, etc.)
are required in this in previous solutions.
What observations can you make about this implementation in terms of efficiency over other solutions?

[The previous version]
    How many operation? : Three operations including Getting user input, handling user input,
    checking whether it is palindrome or not via a recurssive fuction.

[The Dequeing version]
    How many operation? : Four operations including the above three operations and creating a dq_word class.
    For efficiency, honestly speaking, since both versions follow similar operaions,
    I cannot find any noticable differences between two.  
'''


import re

class Deque:
    '''implement Deque class'''
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def add_front(self, item):
        self.item.append(item)

    def add_rear(self, item):
        self.item.insert(0, item)

    def remove_front(self):
        return self.item.pop()

    def remove_rear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

'''From here, creating a palindrome finder'''

def user_input():
    word = raw_input("Enter a word or phrase: ")
    return word

def valid_check():
    word = user_input()
    if re.search(r'\d', word):
        return ""
    elif word.isspace():
        return ""
    else:
        word_adj = []
        for i in word:
            if i.isalpha():
                word_adj.append(i.lower())
    return word_adj

def main(dq_word):
    try:
        if dq_word.size() == 1:
            return "This is a palindrome."
        elif dq_word.size() == 2:
            if dq_word.remove_rear() == dq_word.remove_front():
                return "This is a palindrome."
            return "This is not a palindrome."
        else:
            if dq_word.remove_rear() == dq_word.remove_front():
                return main(dq_word)
            else:
                return "This is not a palindrome."
    except:
        return "Please input a word or pharse!"

if __name__ == "__main__":
    final_word = valid_check()
    dq_word = Deque()
    for i in final_word:
        dq_word.add_front(i)
    print main(dq_word)
