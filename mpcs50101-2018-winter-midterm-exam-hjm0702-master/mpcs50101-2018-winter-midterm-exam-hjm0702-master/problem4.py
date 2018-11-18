# Problem 4:
#
# How many ping pong balls can fit inside a Boeing 747 airplane?
#
# Use the following information to answer the question:
#   - The radius of a ping pong ball is .02 meters
#   - The volume of an Boeing 747 airplane is 1035 cubic meters
#   - The formula for the volume of a sphere is (4/3) * pi * radius^3
#
# In your solution, complete the implementation of the `volume_of_sphere()`
# function below.  The function should return the volume based on the formula
# given above.   You may estimate the value of pi to be 3.14 and assume that
# the argument being passed to the function is a number (e.g. you do not need
# to validate the input.
#
# Write the remainder of the program that calls the function to solve the
# problem.  Pay attention to using best coding practices in your solution.
#
# Print your final answer, the number of ping pong balls, to the standard
# output.
#
#
# If you have time, please let us know where you see yourself in 5 years :)

#Constant numbers
PI = 3.14

# Variables
radius = 0.02
boeing = 1035


def volume_of_sphere(radius):
    volume = (4/3) * PI * radius**3
    return volume

def number_of_sphere(n):
    numbers = boeing / volume_of_sphere(radius)
    return numbers

print number_of_sphere(radius)
