my_foods = ['pizza', 'falafel', 'carrot cake'] #make list of food I like
friend_foods = my_foods[:] #make new list called friend_foods. Make a copy of my_foods by asking for a slice of my_foods 

print('My fav foods are')
print(my_foods)

print('My friends fav foods are')
print(friend_foods)

#prove we are having 2 separte list 

my_foods.append('pho') #adding pho to my_foods list
friend_foods.append('ramen') #adding ramen to friend_foods list

print('My fav foods are')
print(my_foods)

print('My friends fav foods are')
print(friend_foods)

#exercise 4-10 pg116

print(f"The first 3 foods are {my_foods[:3]}")