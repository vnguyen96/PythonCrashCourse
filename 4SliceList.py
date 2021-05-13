players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #prints a slice of this list, which includes just the first three players 

print(players[1:4])

print(players[:4]) #without a starting index, Python starts at the beginning of the lists 

print(players[2:]) #slicing from index 2 to the end of the list

print(players[-3:]) #output last 3 indexes 

#looping through a slice 

print("Here is the first three players on my team: ")
for player in players[:3]:
    print(player.title())
    
