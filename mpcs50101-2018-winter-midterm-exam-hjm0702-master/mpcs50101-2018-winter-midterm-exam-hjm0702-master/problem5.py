# Problem 5
#
# Write a program that calculates a 20% tip for a given dollar amount.
#
# Prompt the user to enter an amount. Using the input, calculate
# the tip and print out the inputed amount, tip and new total.  Use the exact
# format presented below when printing the screen.
#
#      Amount: $10.00
#      Tip: $2.00
#      Total: $12.00
#
# Validate the user input to ensure that the calculations can be completed.  If
# not, print a message to the user that indicates that there was a problem
# with the input and end the program.
#
# The program flow should resemeble the following:
#
#    % python problem4.py
#    Enter a dollar amount? one hundred dollars
#    I was unable to calculate the tip.
#
#
#    % python problem4.py
#    Enter a dollar amount? 100.00
#    Amount: $100.00
#    Tip: $20.00
#    Total: $120.00
#
#

n = raw_input("Enter a dollar amount?")

def tip(n):
    tip = float(n)*0.2
    return tip

def total(n):
    try :
        if float(n) > 0:
            total = float(n) + tip(n)
            '''change print to return if time allows'''
            print "Amount:","$"+str(n)
            print "Tip:", "$"+str(tip(n))
            print "Total:", "$"+str(total)
        else:
            return "The amount must be positive."
    except ValueError:
        return "I was unable to calculate the tip."
    except EOFError:
        return

print total(n)
