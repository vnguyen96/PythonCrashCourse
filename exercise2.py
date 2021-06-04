#exercise 7-4 Pizza topping

message = "\nWelcome to Pizza 'R Us"
message += "\nWhat toppings would you like on your pizza? "

while True: 
    user_input = input(message)

    if user_input == 'quit':
        break
    
    else:
        print(f"We will add {user_input.title()} to your Pizza")

#exercise 7-5 Movie Tickets 

prompt = "\nPlease tell me your age and I will tell you your movie ticket price: "
promt2 = "\nType 'continue' to continue or 'quit' to exit: "

while True:
    message = int(input(prompt))
    
    if message < 3: 
        print("Your ticket is free")
    
    elif 3 < message < 12:
        print("Your ticket price is $10")
    
    else:
        print("Your ticket price is $15")
        
    message2 = input(promt2)

    if message2 == 'quit':
        break

    else:
        continue

message = int

while message < 3: 
    print("Your ticket is free")
    
    if 3 < message < 12:
        print("Your ticket price is $10")
    
    else:
        print("Your ticket price is $15")