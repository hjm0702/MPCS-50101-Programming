fah = raw_input("Enter a temperature in Fahrenheit: ")

try :
    cel = (float(fah)-32)/1.8
    print "It is", cel, "in Celcious.."
#     type(fah) == "str"
#     print "Input must be a number."
except ValueError :
    print "Input must be a number"
#     print "Stupid"
# except :
