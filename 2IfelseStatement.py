age = 17 
if age >= 18:
    print ("You are old enough to vote")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote")
    print("Please register to vote when you turn 18")

print("\n") 
#The if-elif-else Chain 

age = 12 

if age < 4: 
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

print("\n")

#simple approach is to just put the price inside the if-elif-else chain and then have a simple print() call 
age = 12 

if age < 4: 
    price = 0 
elif age < 18:
    price = 25 
else:  
    price = 40 

print(f"Your admission price is ${price}.")
print("\n")

age = 66

if age < 4:
    price = 0 
elif age < 18:
    price = 25
elif age < 65: 
    price = 15 
elif age >= 65:
    price = 20
print(f"Your admission price is ${price}.")
print("\n")

#Testing Multiple conditions

requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushroom.")
if 'sausage' in requested_toppings: 
    print("Adding sausage.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!!!")



