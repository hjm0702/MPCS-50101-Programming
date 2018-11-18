
check = True
while check :
    fah = raw_input("Enter a temperature in Fahrenheit: ")
    try :
        cel = (float(fah)-32)/1.8
        print "It is", cel, "in Celcious.."
        check = False
    #     type(fah) == "str"

    '''as discussed during the class, "except EOFError" clause doesn't work'''

    except:
        print "Input must be a number"
    #     print "Input must be a number."
    except EOFError:
        break
    #     print "Stupid"
    # except :
