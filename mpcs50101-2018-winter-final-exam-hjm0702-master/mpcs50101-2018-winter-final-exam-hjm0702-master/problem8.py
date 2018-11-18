# Problem 8
#
# A) Provide an example of operator overloading implemented in one of Python's
# built-in data types.

__gt__ : > , __lt__ : <, __eq__ : =

# B) Construct a class to implement the abstract data type `Circle`.  The
# `Circle` class should have an attributes named `radius`, `circumference` and
# `area`.  To create an instance of `Circle` write a custom initialization
# function that takes the radius as an argument.  All of the objects attributes
# should be assigned values in the initialization function.
#
# Overload the greater-than and less-than comparision operators to allow
# comparison between `Circle` objects based on their radius.  A `Circle` object
# with a larger radius should be evaluated as greater.  Override the `__str__`
# method to print information about the circle in the following format:
#
#        Cirlce: radius X, circumference Y, area Z

PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
        self.circumference = 2*float(radius)*PI
        self.area = PI*(float(radius)*float(radius))

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False

    def __lt__(self, other):
        if self.radius > other.radius:
            return False
        return True

    def getdata(self):
        return self.radius, self.circumference, self.area

    def __str__(self):

        return "Cirlce: radius "+str(self.getdata()[1]) +", circumference "+ str(self.getdata()[0]) + ", area "+str(self.getdata()[2])

if __name__ == "__main__":
    a = Circle(2)
    print a


# C) Provide a code snippet that creates `Circle` objects that shows
# the comparison operators in use.

PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
        self.circumference = 2*float(radius)*PI
        self.area = PI*(float(radius)*float(radius))

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False

    def __lt__(self, other):
        if self.radius > other.radius:
            return False
        return True

    def getdata(self):
        return self.radius, self.circumference, self.area

    def __str__(self):

        return "Cirlce: radius "+str(self.getdata()[1]) +", circumference "+ str(self.getdata()[0]) + ", area "+str(self.getdata()[2])

if __name__ == "__main__":
    a = Circle(2)
    b = Circle(3)
    print a < b
