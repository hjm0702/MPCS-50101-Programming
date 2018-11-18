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



# C. Write a function that uses a stack to reverse the characters in a string.
