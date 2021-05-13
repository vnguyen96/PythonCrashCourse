#3-4. Make a list of anyone you want to invite to a party 

attendees = ['kung lao', 'liu kang', 'kitana', 'raiden']

for attendee in attendees:
    print(f"{attendee.title()} you are invited to my party")

#print(f"{attendees[0].title()} you are invited to my party")
#print(f"{attendees[1].title()} you are invited to my party")
#print(f"{attendees[2].title()} you are invited to my party")
#print(f"{attendees[3].title()} you are invited to my party")


print('====================================================')

raiden_out = attendees.pop(3) #removing raiden from the list and assign him to raiden_out variable

print(f"{raiden_out.title()}, could not make it to the party...")

attendees.append('sub zero') #adding sub zero to the invitation list

for attendee in attendees:
    print(f"{attendee.title()} you are invited to my party")

#print(f"{attendees[0].title()} you are invited to my party")
#print(f"{attendees[1].title()} you are invited to my party")
#print(f"{attendees[2].title()} you are invited to my party")
#print(f"{attendees[3].title()} you are invited to my party")

print('====================================================')

for attendee in attendees:
    print(f"{attendee.title()} you are invited to my party")
    
#print(f"{attendees[0].title()} you are invited to my party")
#print(f"{attendees[1].title()} you are invited to my party")
#print(f"{attendees[2].title()} you are invited to my party")
#print(f"{attendees[3].title()} you are invited to my party")

print('====================================================')

for attendee in attendees:
    print(f"{attendee.title()} I have found a larger table")

#print(f"{attendees[0].title()} I have found a larger table")
#print(f"{attendees[1].title()} I have found a larger table")
#print(f"{attendees[2].title()} I have found a larger table")
#print(f"{attendees[3].title()} I have found a larger table")

print('====================================================')

attendees.insert(0, 'scorpian')
attendees.insert(3, 'jade')
attendees.append('mileena')

for attendee in attendees:
    print(f"{attendee.title()} you are invited to my party")

#print(f"{attendees[0].title()} you are invited to my party")
#print(f"{attendees[1].title()} you are invited to my party")
#print(f"{attendees[2].title()} you are invited to my party")
#print(f"{attendees[3].title()} you are invited to my party")
#print(f"{attendees[4].title()} you are invited to my party")
#print(f"{attendees[5].title()} you are invited to my party")
#print(f"{attendees[6].title()} you are invited to my party")

print(len(attendees))
print('====================================================')

print("My bigger table wont be arrive on time I can only invite 2 people")

millena_out = attendees.pop()
print(f"Sorry {millena_out.title()} I could not invite you")

subzero_out = attendees.pop()
print(f"Sorry {subzero_out.title()} I could not invite you")

kitana_out = attendees.pop()
print(f"Sorry {kitana_out.title()} I could not invite you")

jade_out = attendees.pop()
print(f"Sorry {jade_out.title()} I could not invite you")

print("Here is the original list:")
liukang_out = attendees.pop()
print(f"Sorry {liukang_out.title()} I could not invite you")

del attendees[0]

del attendees[0]

print(attendees)