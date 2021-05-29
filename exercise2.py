#ex 5-3

alien_color = 'red'

if alien_color is 'green':
    print("Alien color is green")
if alien_color is 'red':
    print("Alien color is red. You earned 5 points")
if alien_color is 'yellow':
    print("Alien color is yellow")

#ex 5-4 


alien_color = 'yellow'

if alien_color is 'green': 
    print("Alien color is green. You earned 5 points") 
elif alien_color is 'yellow':
    print("alien color is yellow. You earned 10 points")
else:
    print("Alien color is red. You earned 15 points!!")


#ex 5-6 stages of life 

age = 24

if age < 2:
    print("The person is a baby")
if 2 <= age < 4: 
    print("The person is a toddler")
if 4 <= age < 13:
    print("The person is a kid")
if 13 <= age < 20:
    print("The person is a teenager")
if 20 <= age < 65:
    print("The person is an adult")
if age >= 65:
    print("The person is an elder")

#ex 5-7 Favorite fruits 

fav_fruits = ['orange', 'banana', 'mango']

if 'apple' in fav_fruits:
    print("You don't like this fruit")
if 'orange' in fav_fruits: 
    print("You really like orange")
if 'banana' in fav_fruits:
    print("You really like bananas")
if 'mango' in fav_fruits:
    print("You really like mangos") 
if 'coconut' in fav_fruits:
    print("You don't like this fruit")


