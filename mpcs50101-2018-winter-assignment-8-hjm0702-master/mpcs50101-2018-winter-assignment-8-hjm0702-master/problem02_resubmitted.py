import re
from problem01 import Stack

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
