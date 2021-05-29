#5-8 Hello Admin

users = [] 

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else: 
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users") 


print("\n")
 
#5-10 Checking Usernames #272

current_users = ['dschup', 'vnguyen', 'bneume', 'jsim', 'swah'] 

new_users = ['fgrani', 'ssimp', 'jsim', 'swah', 'bthomas']

for user in current_users:
    if user in new_users:
        print(f"You need to pick a new username beside {user}")
    else:
        print(f"{user} is available")

print("\n")
 
#5-11 Ordinal numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

for number in numbers: 
    if number == 1:
        print("1st") 
    elif number == 2:
        print("2nd")
    elif number == 3: 
        print("3rd")
    else: 
        print(f"{number}th")

