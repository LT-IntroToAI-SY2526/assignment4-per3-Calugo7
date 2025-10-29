# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A Simple Dog class to learn Object Oriented Program
    
    Attributes:
        fur_coler = the color of the dogs fur
        name = the name of the dog
        age = the age of the dog
        favorite_food = the dog's favorite food
        """
    "Constructor"
    "self = this"
    def __init__(self, fur_color, name, age, favorite_food):
        """initialize a new Dog wit fu_color, name, age, and favorite_food"""
        self.fur_color = fur_color
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def __str__(self):
        "return a string rep of dog"
        return f"{self.name} is a {self.age} year old {self.fur_color} dog who loves {self.favorite_food}"
    
    def bark(self):
        """make the dog bark"""
        return f"{self.name} says woof woof!!"
    
my_dog = Dog("black", "Logan", 9, "salmon")
enggy_dog = Dog("black and white", "peluchin", 13, "rice")

print (enggy_dog.__str__())

print (enggy_dog.bark())
print (my_dog.bark())