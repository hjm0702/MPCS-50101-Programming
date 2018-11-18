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
    check = True
    if isinstance(a, int) == False or isinstance(b, int) == False:
        print "Input must be an integer."
    elif b == 0:
        print "The secound number must be a non-zero integer."
    elif a == b:
        check = False
        return check
    elif a % b != 0:
        check = False
        return check
    else:
        power(a/b,b)
        return check
#     print hi
# # def power(a,b):
# #     if a % b == 0:
# #         return True
# #     else:
# #         return power(a/b,b)

print power(64, 64)
# print 64 % 5
