'''How to handle if instance has no value???'''


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
    #

def greater_than(f1,f2):
    if substract_them(f1,f2) > 0:
        return "The first fraction is greater than the second."

def less_than(f1, f2):
    if substract_them(f1,f2) < 0:
        return "The first fraction is less than the second."
    #
def as_decimal(self):
    """Print a fraction object instance as a decimal.  Precision to 3 decimal places is sufficient"""
    try:
        return round((self.a*0.01)/(self.b*0.01),3)
    except:
        return


def main():
    def add(a,b):
        print add_them_up(a, b), as_decimal(add_them_up(a, b))

    def substract(a,b):
        print substract_them(a,b), as_decimal(substract_them(a,b))

    def multiply(a,b):
        print multiply_them(a,b), as_decimal(multiply_them(a,b))

    def divide(a,b):
        print divide_them(a,b), as_decimal(divide_them(a,b))

    userinput = "4/59 / 3/60"
    split = userinput.split(' ')
    first = split[0].split("/")
    second = split[2].split("/")
    # print first,second, split[1]
    # if first[0].isdigit() == False or first[1].isdigit() == False or first[1] =="0":
    #     print "Please input a valid form of fraction"
    # if second[0].isdigit() == False or second[1].isdigit() == False or second[1] =="0":
    #     print "Please input a valid form of fraction"
    try:
        f1 = Fraction(int(first[0]),int(first[1]))
        f2 = Fraction(int(second[0]),int(second[1]))
        # print f1, f2
    except:
        print "Please input a valid form of fraction"

    if split[1] == "+":
        add(f1,f2)
    if split[1] == "-":
        substract(f1,f2)
    if split[1] == "*":
        multiply(f1,f2)
    if split[1] == "/":
        divide(f1,f2)

    # f1_1 = Fraction(1,2)
    # f1_2 = Fraction(3,4)
    # f2_1 = Fraction(1,100)
    # f2_2 = Fraction(2,100)
    # f3_1 = Fraction(9,12)
    # f3_2 = Fraction(1,16)
    # f4_1 = Fraction(4,21)
    # f4_2 = Fraction(4,29)
    # f5_1 = Fraction(1,10)
    # f5_2 = Fraction(1,2)
    # f6_1 = Fraction(3,4)
    # f6_2 = Fraction(4,3)
    # f7_1 = Fraction(1,16)
    # f7_2 = Fraction(1,32)
    # f8_1 = Fraction(4,59)
    # f8_2 = Fraction(3,60)

    # print add(f1_1, f1_2)
    # print as_dicimal(f1_1)

    # add(f1_1,f1_2)
    # add(f2_1,f2_2)
    # substract(f3_1,f3_2)
    # add(f4_1,f4_2)
    # divide(f5_1,f5_2)
    # multiply(f6_1,f6_2)
    # multiply(f7_1,f7_2)
    # divide(f8_1,f8_2)



if __name__ == "__main__":
    main()
