#Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later 

#Moving Items from One List to Another 

    #Start with uers that need to be verified 
    #another empty list with confirmed users 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

    #Verified each user util there are no more unconfirmed users 
    #Move each verified user into the list of confirmed users 

while unconfirmed_users: #The while loop runs as long as the list 'unconfirmed_users' is not empty. 
    current_user = unconfirmed_users.pop() #Pop method removes unverified users one at a time from the end of 'unconfirmed_users'. Since Candace is last her name will be removed first

    print(f"\nVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)

    #Display all confirmed users. 
    print("\nThe following users have been confirmed: ")

    for confirmed_user in confirmed_users: 
        print(confirmed_user.title())    

#Removing All Instances of Specific Values from a List 

pets = ['dog', 'cat', 'fish', 'rabbit', 'cat', 'hamster', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#Filling a dictionary with user input 

responses = {}

    #Set a flag to indicate that polling is active 

polling_active = True 

while polling_active: 
    #Prompt for the person's name and response
    name = input ("\nWhat is your name?")

    response = input("Which mountain would you like to climb today?")

    #Store the response in the dictionary 'responses' with key and value 
    responses[name] = response

    #Find out if anyone else is going to take the poll 
    repeat = input("Would you like to let another person respond? (yes/no)")
    
    if repeat == 'no':
        polling_active = False 
   
    #Polling is complete. Show the results. 
    for name, response in responses.items():
        print(f"{name.title()} would like to climb {response.title()}")

