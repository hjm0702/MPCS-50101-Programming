def grade():
    input = raw_input("> Enter a score: ")
    try:
        if isinstance(float(input), float):
            if float(input) >=90 and float(input) <= 100:
                print "You received an A!"
            elif float(input) >=80 and float(input) < 90:
                print "You received a B!"
            elif float(input) >= 70 and float(input) < 80:
                print "You received a C!"
            elif float(input) >= 60 and float(input) < 70:
                print "You received a D!"
            elif float(input) <60 and float(input) >=0:
                print "You received a F!"
            else:
                print "A score must be between 0 and 100."
    except:
        print "A score must be a number."

print grade()
