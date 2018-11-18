# Problem 3


class Animal:
    latin_name = "Canis lupus familiaris"

class Dog(Animal):

    def __init__(self):
        self.latin_name = "Rufus"


# Using the above class, evaluate what each of the following statements will
# print? Will it be the same?  If not, explain what is going on with the
# variable `latin_name`.
#
#   Dog.latin_name
#   Dog().latin_name
#
