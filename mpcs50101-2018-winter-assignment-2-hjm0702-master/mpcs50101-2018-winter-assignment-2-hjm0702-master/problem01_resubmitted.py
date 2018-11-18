
def temp_converter(input):
    input = raw_input("> Enter a temperature in Fahrenheit: ")
    # if isinstance(type(input), float) == False:
    try :
        if isinstance(float(input), float):
            temp = (float(input)-32)/1.8
            print "It is", temp, "in Celcious.."
    except:
        print "You should enter a number."

print temp_converter(input)
