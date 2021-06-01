#Looping through all key-values pairs pg296

user_0 = {
    'username': 'efemi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items(): #for loop, create names for the 2 variables in each key-value pair in this case its 'key' and 'value'. Method .items() returns a list of key-value pairs
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print("\n")


fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in fav_languages.items():
    print(f"{name.title()} favorite language is {language.title()}")
print("\n")


#Looping through all the keys in a dictionary  #300

    #The key() methods is useful when you dont need to work with all of the values in a dictionary 

for name in fav_languages.keys(): #tell python to pull all the keys from the dictionary fav_languages and assisn them one at a time to the variable 'name'
    print(f"{name.title()}")
print("\n")



friends = ['phil', 'sarah'] #make list of friends we want to print a message to. Inside the loop, we print each person's name

for name in fav_languages.keys(): 
    print(f"Hi {name.title()}")

    if name in friends: #check whether the 'name' we're working with is in the list 'friends'
        language = fav_languages[name].title() #if it is, we determine the person's fav language using the name of the dictionary and the current value of 'name' as the key
        print(f"\t{name.title()}, I see you love {language}")

if 'erin' not in fav_languages.keys():
    print('Erin please take our poll')
print("\n")


#Looping through a dictionary's keys in particular order pg 303

for  name in sorted(fav_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print("\n")


#Looping through all values in a dictionary 

print("The following languages have been mentioned:")
for language in sorted(fav_languages.values()):
    print(language.title())  #this code will print 'Python' twice
print("\n")


print("The following languages have been mentioned:")
for language in set(sorted(fav_languages.values())): #A 'set' is a collection in which each item must be unique
    print(language.title())





