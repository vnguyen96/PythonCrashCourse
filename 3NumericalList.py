#using range() function 


for value in range(1, 5): #this will only print 1-4. This is result in off-by-one behavior see often in programming languages 
    print(value)

for value in range(1, 6): #this will print 1-5
    print(value)


#using range() to Make a List of Numbers 

numbers = list(range(1, 6))
print(numbers)

#making a list of even numbers between 1 and 10 

even_numbers = list(range(2, 11, 2)) #the range function starts with the value 2 and then adds 2 to that value 
print(even_numbers)

#making a list of square number from 1 to 10

squares = [] #starts with empty list
for value in range(1, 11): #tell Python to loop thru each value from 1 to 10 using the range() function
    square = value ** 2 #the current value is raised to thee second power and assigned to the variable square 
    squares.append(square) #each new value of square is appended to the list squares 
print(squares) #when the loop has finished running, the list of squares is printed 

#to write this code more concisely, omit the temoporary variable square and append each new value directly to the list: 

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#List Comprehensions 

squares = [value**2 for value in range(1, 11)]
print(squares)