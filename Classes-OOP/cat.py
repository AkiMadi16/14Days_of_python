class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# This code defines a class named Cat, which has two attributes: color and legs.
# Then the class is used to create 3 separate objects of that class.

# In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.

print(felix.color)
# ginger

# the __init__ method takes two arguments and assigns them to the object's attributes. The __init__ method is called the class constructor.
