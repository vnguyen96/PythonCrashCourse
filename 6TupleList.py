#Python refers to values that cannot change as immutable, and an immutable list is called a tuple

#A tuple looks just like a list except you use parenthese instead of square brackets 

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250 #this wont work 

print("Original dimensions:")
for dimension in dimensions: 
    print(dimension)

dimensions = (400, 100)
print("New dimensions:")
for dimension in dimensions: 
    print(dimension)


#exercise 4-13 

menu = ('pizza', 'hot dog', 'burger', 'tacos', 'pasta')

for food in menu:
    print(food)

#menu[1] = ('pho')

menu = ('sushi', 'hot dog', 'burger', 'tacos', 'pasta')

for food in menu:
    print(food)

