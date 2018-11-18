# print isinstance('asd', int)
#
# def power(a,b):
#     if isinstance(a, int) == False or isinstance(b, int) == False:
#         print "Input must be an integer."
#     elif a % b == 0:
#         if (a/b) % b == 0:
#             return True
#         else:
#             return False
#     else:
#         return False


def power(a,b):
    # check = True
    '''handling user input'''
    if isinstance(a, int) == False or isinstance(b, int) == False:
        return "Input must be an integer."
    elif b == 0:
        return "The secound number must be a non-zero integer."
    '''main fuction'''
    elif b == 1:
        if a == 1:
            return check
        else:
            return "The secound number must be an integer greater than 1."
    else:
        if a % b != 0:
            print False
        elif a == b:
            print True
        else:
            # print a,b
            power(a/b,b)

print power(10000,10)
    # else:
    #     return 'hi'
        #
        # while check:
        #     if a % b != 0:
        #         check = False
        #         return check
        #     elif a == b:
        #         return check
        #     else:
        #         power(a/b,b)
        #         # return check


#     print hi
# # def power(a,b):
# #     if a % b == 0:
# #         return True
# #     else:
# #         return power(a/b,b)


# print 64 % 5
