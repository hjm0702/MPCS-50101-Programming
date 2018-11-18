import random
# import math

class Fraction:
    '''count fraction
    instance : a Fraction
    method : each mathematical operations'''

    def __init__(self, a, b):
        if isinstance(a, int) == True:
            self.a = a
        else:
            self.a = "Please input an integer for %s." % (a)
        if isinstance(b, int) == True:
            if b != 0:
                self.b = b
            else:
                self.b = "Please input a non-zero integer."
        else:
            self.b = "Please input an integer for %s." % (b)
    #

    def __str__(self):
        '''print them in a Slash form (3/5) or (1-1/4)'''
        if self.a == 0 :
            return 0
        elif self.a * self.b < 0:
            if abs(self.a) >=abs(self.b):
                if divmod(abs(self.a),abs(self.b))[1] !=0:
                    return "%s-%s/%s" %(divmod((self.a),(self.b))[0], divmod((self.a),(self.b))[1], abs(self.b))
                else:
                    return "%s" %(divmod((self.a),(self.b))[0])
            else:
                return "%s/%s" %(-1*abs(self.a), abs(self.b))


        elif self.a * self.b :
            if abs(self.a) >= abs(self.b):
                if divmod(abs(self.a),abs(self.b))[1] !=0:
                    return "%s-%s/%s" %(divmod(abs(self.a),abs(self.b))[0], divmod(abs(self.a),abs(self.b))[1], abs(self.b))
                else:
                    return "%s" %(divmod(abs(self.a),abs(self.b))[0])#abs(self.a)%abs(self.b)
            else:
                return "%s/%s" % (abs(self.a),abs(self.b))
            #
            #  >= abs(self.b):
            # return

def greated_common_divisor(a, b):
    if abs(a) == abs(b):
        return a
    elif min(abs(a),abs(b)) == 0 :
        return max(abs(a),abs(b))
    else:
        return greated_common_divisor(min(abs(a),abs(b)), (max(abs(a),abs(b)) % min(abs(a),abs(b))))

def add_them_up(f1, f2):
    '''add two fractions'''
    try:
        add = Fraction(0,0)
        add.a = f1.a*f2.b+f2.a*f1.b
        add.b = f1.b*f2.b
        c = greated_common_divisor(add.a, add.b)
        # print add.a, add.b, c
        add.a = add.a / c
        add.b = add.b / c
        return add
    except :
        return "Please input a valid integer."



def substract_them(f1, f2):
    '''substract two fractions'''
    try:
        sub = Fraction(0,0)
        sub.a = f1.a*f2.b-f2.a*f1.b
        sub.b = f1.b*f2.b
        c = greated_common_divisor(sub.a, sub.b)
        # print sub.a, sub.b, c
        sub.a = sub.a / c
        sub.b = sub.b / c
        return sub
    except:
        return "Please input a valid integer."

def multiply_them(f1,f2):
    '''multiply two fractions'''
    try:
        mul = Fraction(0,0)
        mul.a = f1.a*f2.a
        mul.b = f1.b*f2.b
        c = greated_common_divisor(mul.a, mul.b)
        # print mul.a, mul.b, c
        mul.a = mul.a / c
        mul.b = mul.b / c
        return mul
    except :
        return "Please input a valid integer."

def divide_them(f1,f2):
    '''divde two fraction'''
    try:
        div = Fraction(0,0)
        div.a = f1.a*f2.b
        div.b = f1.b*f2.a
        c = greated_common_divisor(div.a, div.b)
        # print div.a, div.b, c
        div.a = div.a / c
        div.b = div.b / c
        return div
    except :
        return "Please input a valid integer."

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b :
            return True
        return False

f1 = Fraction(1,2)
f2 = Fraction(1,2)
print f1.a, f2.a
print f1 == f2

def main():
    print "Welcome to Action Fraction!"

    again = True
    while again:
        random_operation = random.choice(["+", "-", "*", "/"])
        '''random integer range from 1 to 100 for a reasonable difficuly of calcualation'''
        f1_1 = random.randint(1,10)
        f1_2 = random.randint(1,10)
        f2_1 = random.randint(1,10)
        f2_2 = random.randint(1,10)

        # print random_operation, a
        f1 = Fraction(f1_1,f1_2)
        f2 = Fraction(f2_1,f2_2)

        answer = raw_input ("What is %d/%d %s %d/%d?" %(f1_1, f1_2, random_operation,f2_1,f2_2))
        try :
            answer_split = answer.split("/")
            answer_Frac = Fraction(int(answer_split[0]),int(answer_split[1]))
            print answer_Frac
        except:
            print "Please input a valid form of fraction."
        # answer_Frac =
        # print f1
        # print f2

        actual_answer = Fraction(0,0)

        if random_operation == "+":
            actual_answer = add_them_up(f1,f2)
        if random_operation == "-":
            actual_answer = substract_them(f1,f2)
        if random_operation == "*":
            actual_answer = multiply_them(f1,f2)
        if random_operation == "/":
            actual_answer = divide_them(f1,f2)

        total_try = 0
        correct = 0
        print actual_answer

        if actual_answer == answer_Frac:
            total_try += 1
            correct += 1
            ask_yes = raw_input("Correct!  Would you like another problem [y/n]?")

        else:
            total_try += 1
            ask_no = raw_input("Incorrect!  Would you like another problem [y/n]?")

        if ask_no.islower() == "n" or ask_yes.islower() == "n":
            print "You answered %d/%d problems correctly.  Keep up the good work!" %(correct, total_try)
            again = False


# print main()
    # problem02.add_them_up(4/59 / 3/60)

    # again = True:
    # while again:



if __name__ == "__main__":
    main()
