#A function doesn't always display its output directly. Instead, it can process some data and then return a value or set of values
# The value the function returns is called a return value

#Return a Simple Valuee

def get_formatted_name(first_name, last_name): #take first and last name as parameters
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}" #function combines these 2 names, adds a space between, and assigns to 'full_name' 
    return full_name.title() #Value of full_name is converted to title case, and then returned to the calling line

musician = get_formatted_name('jimi', 'hendrix') #When calling a function that returns a value, you need to provide a variable that the return value can be assigned to
print(musician)

#Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name=""): 
    if middle_name: #Python interprets non-empty string as True 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('david', 'gilmore')
musician = get_formatted_name('david', 'hooker', 'lee')

print(musician)

#Returning a Dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('david', 'gilmore')
print(musician)


def build_person(first_name, last_name, age=None): #None evaluates to False
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('david', 'gilmore', age=70)
print(musician)


#Using a Function with a while Loop

def get_formatted_name(first_name, last_name): 
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}")


    exit_program = input("Type 'q' to quit: ")

    if exit_program == 'q':
        break
 



