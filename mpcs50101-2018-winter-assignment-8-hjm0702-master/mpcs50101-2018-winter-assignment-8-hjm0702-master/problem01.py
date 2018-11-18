'''unit test file attached seperately'''

class Stack:
    '''Implement Stack Class'''
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

def userinput():
    print "Enter the source code. Type Ctrl-Z to submit."
    contents = []
    final_input = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)

    final_input = "".join(contents)
    return final_input



def balancer(n):
    stacklist = Stack()
    push_pop_dict = {"(" : ")", "{" : "}", "[" : "]"}
    balanced = True
    # for i in userinput():

    if n == None:
        print "no"

    for i in n:
        if i in push_pop_dict.keys():
            stacklist.push(i)
        elif i in push_pop_dict.values():
            if i == push_pop_dict[stacklist.peek()]:
                stacklist.pop()
            else:
                balanced = False

    if not stacklist.isEmpty():
        balanced = False

    if balanced == False:
        return "Symbols are not balanced :("
    else:
        return "Symbols are balanced!!!! :)"

if __name__ == "__main__":
    n = userinput()
    print balancer(n)


# if __name__ == "__main__":
#     test = Stack()
#     print test.isEmpty()
# #     test.push("hi")
#     print test
#     test.push(2)
#     test.push(3)
#     test.push("asddsaf")
#     print test.size()
#     print test.getdata()
#     print test.peek()
#     # print test.getdata()
#     test.pop()
#     print test.getdata()
#     print test.size()
#     print test.isEmpty()
