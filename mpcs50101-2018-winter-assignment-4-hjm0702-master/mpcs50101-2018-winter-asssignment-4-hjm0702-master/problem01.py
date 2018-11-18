
#


def temperature(fah):
    try :
        cel = (float(fah)-32)/1.8
        return cel
    except EOFError :
        return "Please input something"
    except ValueError :
        return False
        # return "You should input a number"
#

if __name__ == "__main__":
    fah = raw_input("Enter a temperature in Fahrenheit: ")
    print temperature(fah)



# if temperature(fah) != False:
#     print "It is", temperature(fah), "in Celcious."
# else:
#     print temperature(fah)




# # except :
