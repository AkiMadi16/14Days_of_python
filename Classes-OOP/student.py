# create a class and its constructor, taking one argument and assigning it to the "name" attribute. Then create an object of the class.
class Student:
    def __init__(self, name):
        self.name = name


test = Student("Bob")
print(test.name)
