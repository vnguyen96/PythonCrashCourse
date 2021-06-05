#>>Positional Arguments

    #When calling a function, Python must match each arguments in the fuction call with a parameter in the fuction definition 

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#>>Multiple function calls 

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#>>Keyword Arguments 

    #Keyword argument is a name-value pair that you pass to a function. This will avoid confusion 

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name = 'harry')


#>>Default Values 

    #If an argument for a parameter is provided in the function call, Python uses the argument value, if not, it sus the parameter's default value

def describe_pet( pet_name, animal_type = 'dog',):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet(pet_name = 'willie')

    #When using default values, any parameter with a default value needs to be listed after all the parameters that don't have any default values

#Equipvalent Function Calls 

#Avoiding Arguments Errors 

def describe_pet( pet_name, animal_type = 'dog',):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name.title()}.")

describe_pet() 