name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#Sometimes you'll want to write a prompt that's longer than one line.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?" # operator += takes the strong that was assigned to 'prompt' and adds the new string onto the end

name = input(prompt)
print(f"\nHello, {name}!")


#Using int() to Accept Numerical Input

#Python interprets everything the user enters as a string

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")
print("\n")

# The Modulo Operator which devides one number by another number and returns the remainder 

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: 
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")ds