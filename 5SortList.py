

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sort() method
print(cars) 

'''cars.sort(reverse = True) #sort and reverse the list
print(cars)'''

#Sorting a List Temporarily with the sorted() function 

colors = ['blue', 'red', 'amber', 'purple']
print(colors)

print("Here is the sorted list:")
print(sorted(colors)) 

print("Here is the orignial list again:")
print(colors)

#finding length of a list 

print(len(colors))


for color in colors: 
    print(f"{color} is the color")