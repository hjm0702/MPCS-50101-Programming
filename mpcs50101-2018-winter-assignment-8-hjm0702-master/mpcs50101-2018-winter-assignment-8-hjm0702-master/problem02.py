import re

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
    '''handling userinput'''
    userinput = raw_input("Please input an integer. : ")
    try:
        if isinstance(int(userinput), int):
            return userinput
    except:
        print "Please input an integer!!"

def binary(n):
    '''calculate a binary number'''
    try:
        number = int(n)
        if number >=0:
            if n == 0:
                for i in range(stack.size()):
                    final_number.append(str(stack.pop()))

            else:
                stack.push(divmod(number, 2)[1])
                binary(divmod(number, 2)[0])
        elif number <0:
            number = abs(number)
            if n == 0:
                for i in range(stack.size()):
                    final_number.append(str(stack.pop()))
            else:
                stack.push(divmod(number, 2)[1])
                binary(divmod(number, 2)[0])

            final_number.insert(0,"-")
    except:
        return ""

if __name__ == "__main__":
    n = userinput()
    stack = Stack()
    final_number = []
    binary(n)
    print "".join(final_number)
