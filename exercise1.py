#7-1 Rental car ph 365 

car = input("\nWhat car are you looking for? ")
print(f"\nLet me see if I can find {car} model")
print("\n")
#7-2 Restaurant Seating 

numb_people = input("How many peopl are in your party? ")
numb_people = int(numb_people)

if numb_people > 8:
    print("\nPlease wait for table")
else: 
    print("\nYour table is ready")