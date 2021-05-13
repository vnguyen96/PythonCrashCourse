#using for loop to print out each name in a list 

magicians = ['alex', 'david', 'carolina']

for magician in magicians:
    print(magician)
   
#doing more with for loop 

for magician in magicians: 
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}")

print("Thank you everyone that was a great magic show")






