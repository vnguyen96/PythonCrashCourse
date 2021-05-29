requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are about of green peppers") 
    else:
        print(f"Adding {requested_topping}")
print("\nYour pizza is ready")
print("\n")

#Check to see if the list is empty 

requested_toppings = [] #1 start with empty list

if requested_toppings: #2 Quick check before jumping into for loop 
    for requested_topping in requested_toppings: 
        print(f"Adding {requested_topping}")
        print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")
print("\n")

#Using multiple lists 

available_toppings = ['mushroom', 'green peppers', 'extra cheese']

requested_toppings = ['mushroom', 'french fries', 'extra cheese'] 

for requested_topping in requested_toppings: # Loop thru the list of requested toppings. Check to see if each requested toppings is actually in the list of available toppings  
    if requested_topping in available_toppings: # If it is we adding topping to the pizza 
        print(f"Adding {requested_topping}")
    else: 
        print(f"{requested_topping.title()} is not available")
print("Finished making your pizza") 


