score = raw_input("Enter a score :")
if float(score) >100 or float(score)<0:
    print "The score is out of scope!"
elif float(score) >= 90:
    print "You received an A"
elif float(score) >=80:
    print "You received a B"
elif float(score) >=70:
    print "You received a C"
elif float(score) >=60:
    print "You received a D"
elif float(score) <60 and float(score) >0: 
        print "You received an F"
