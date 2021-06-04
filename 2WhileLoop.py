current_number = 1 
while current_number <= 5: #while loop is set to keep running as long as the value of current bynber is less than or equal to 5
    print(current_number) 
    current_number += 1 # operator '+=" is shorthand for current_number = current_number + 1

#Letting the User Choose When to Quit

promt = "\nTell me something, and I will repeat it back to you: " #definning promt with 2 options
promt += "\nEnter 'quit' to end the program. "

message = "" #create variable to track value the user enters 

while message != 'quit':
    message = input(promt)

    if message != 'quit':
        print(message)


#Using a Flag

promt = "\nTell me something, and I will repeat it back to you: " 
promt += "\nEnter 'quit' to end the program. "

active = True #set variable active to True 

while active: 
    message = input(promt)

    if message == 'quit': #If user enters 'quit', we set active to False. and the while loop stops
        active = False
    
    else:
        print(message) #If user enters anything other an 'quit, we print thier input as a message

#Using Break to Exit a Loop

    #break exit loop immediately without running any remaining code in the loop, regardless of the results of any conditional test

promt = "\nPlease enter the number of cities you have visited: "
promt += "\nEnter 'quit when you are finished. " 

while True: # loop that starts with 'while True' will run forever unless it reaches a 'break' statement 
    message = input(promt)

    if message == 'quit':
        break

    else:
        print(f"I'd love to go to {message.title()}!")

#Using 'Continue' in a Loop
print("\n")
current_number = 0 
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Avoiding Infinite loops 

x = 1 
while x <= 5:
    print(x)
    # x += 1 <<< this code will continue to loop if this line is missing


