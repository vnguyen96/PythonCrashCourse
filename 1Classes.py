#In object-oriented programming you write classes that represent real-world things and situations, you create objects based on these classes 

#Making an object from a class is called instantiation, and you work with instances of a class

#Creating and using a class 

class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age): #Defining __init__ method. A function in a class is a method. __x__ is Python's default method
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")