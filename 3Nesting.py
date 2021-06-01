#A list of dictionaries 

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens: 
    print(alien)
print("\n")

#A more realistic example would involve more than three aliens with code that automatically generates each alien

    #Make an empty list for sorting aliens 
aliens = []

    #Make 30 green aliens 
for alien_number in range(30): #range() returns a series of number, which just tells Python how many times wee want to loop to repeat
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #Eeach time the loops runs, we create a new alien 
    aliens.append(new_alien) #and then append each new alien to the list 'aliens'

    #Change the first 3 aliens color to yellow
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    #Show the first 5 aliens
for alien in aliens[:5]: #use a slice to print the first five aliens
    print(alien)
print("...")

    #Show how many aliens have been created. 
print(f"Total number of aliens:{len(aliens)}") #print the length of the list 
print("\n")
    #Each aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually 


#A List in a Dictionary 

    #Store information about a pizza being ordered 

pizza = {          #Dictionary holds info about a pizza that has been ordered 
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

    #Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " #Summarize the order before building the pizza 
        "with the follow toppings:") 

for topping in pizza['toppings']: #To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary. 
    print(f"\t{topping}")
print("\n")



fav_languages = { #Value associated with each name is now a list
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in fav_languages.items(): #When looping thru the dictionary, we use variable name 'languages' to hold each value from the dictionary
    
    if len(languages) <= 1: #Check to see if the value of is list is less than 1
        print(f"\n{name.title()} favorite languages is: ")
    
    else:
        print(f"\n{name.title()} favorite languages are: ")


    for language in languages: #Loop run through each person's list of fav languages
         print(f"\t{language.title()}")



#A Dictionary in a Dictionary 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items(): #Loop thru the users dictionary. Python assigns each key to the variable 'username', and the dictionary associated with each usename is assigned to the variable user_info
    print(f"\nUsername: {username}") #Once inside the main dictionary loop, we print the username 

    full_name = f"{user_info['first']} {user_info['last']}" #Start accessing the inner dictionary 
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")