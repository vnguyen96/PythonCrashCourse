#7-8 Deli 

sandwich_orders = ['bmt', 'banh mi', 'pb&j', 'philly cheese', 'grilled cheese']

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    print(f"\nI made your {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

print(f"\nThe following sandwiches have been made: ")
for sandwich_order in finished_sandwiches:
    print(sandwich_order)
print("\n")

#7-9 no more Pastrami

sandwich_orders = ['bmt', 'banh mi', 'pb&j', 'pastrami', 'philly cheese', 'pastrami', 'grilled cheese', 'pastrami']

print("The deli has ran out of pastrami sandwich")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10 Dream vacations

dream_vacations = {}

while True: 
    name = input("\nWhat is your name? ")
    place = input("\nWhere is your dream vacation? ")

    dream_vacations[name] = place

    repeat = input("\nDo you want to let another person to yestering the info? (yes/no): ")
    
    if repeat == 'no':
        break

    for name, place in dream_vacations.items():
        print(f"\nHello {name.title()}, your dream vacation is {place.title()}")
