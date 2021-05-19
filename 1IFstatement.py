cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#CONDITIONAL TESTS 

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("\nHold the anchovies!")



answer = 17 

if answer != 42:
    print("\nThat is not the correct answer. Please try again!")



#Checking weather a value is in a list 

requested_topping = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_topping)

print('pepperoni' in requested_topping)


#Checking weather a value is not in a list 

banned_users = ['andrew', 'carolina', ' david']
user = 'marie'

if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish")
