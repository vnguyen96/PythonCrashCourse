#In object-oriented programming you write classes that represent real-world things and situations, you create objects based on these classes 

#Making an object from a class is called instantiation, and you work with instances of a class

#Creating and using a class 

class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age): #Defining __init__ method. A function in a class is a method. __x__ is Python's default method
        self.name = name #variables that accessible through instances like this are called attributes 
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")


#Making an Instance from a Class 

    #Think of a class as a set of instructions for how to make an instance 

my_dog = Dog('Willie', 6) #my_dog is a single instance create from class 

print(f"My dog's name is {my_dog.name}.") #Here Python looks at the instance my_dog and then finds the attribute name associated with my_dog. This is the same attribute referred to as self.name in class Dog
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()


#Creating multiple instances 

my_dog = Dog('Willie', 6) 
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"You dog is {your_dog.age}.")
your_dog.sit()