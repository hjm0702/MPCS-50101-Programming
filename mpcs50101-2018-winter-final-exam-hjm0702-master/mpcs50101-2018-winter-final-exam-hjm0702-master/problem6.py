# Problem 6

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


# A. Given the above class definition of a stack data type, what will be the
# top item on the stack when the sequence is complete?
#
# m = Stack()
# m.push('ʕ•ᴥ•ʔ')
# m.peek()
# m.push('ᕕ( ᐛ )ᕗ')
# m.pop()
# m.push('(⊙_☉)')
# m.push('¯\_(ツ)_/¯')
# m.push('◔_◔')
# m.peek()
# m.pop()
# m.peek()

Answer : ¯\_(ツ)_/¯

# B. Given the following sequence of stack operations, what will be output when
# the sequence is complete?
#
# m = Stack()
# m.push('( ͡° ͜ʖ ͡°)')
# m.push('ಠ_ಠ')
# m.push('( •_•)')
# while not m.isEmpty():
#    m.pop()
#    m.pop()
# m.peek()

[] since the line 47~49 will pop all of the items in m until m is empty.

# C. Write a function that uses a   stack to reverse the characters in a string.


class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def __str__(self):
         return str(self.items)

if __name__ == "__main__":
    word = "abcde"
    reversed_word = Stack()
    popped_word = Stack()
    for i in word:
        reversed_word.push(i)

    for j in range(reversed_word.size()):
        popped_word.push(reversed_word.pop())

    print str(popped_word)
