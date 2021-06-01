#6-5 pg 308 Rivers

famous_river = {'nile': 'egypt', 'amazon': 'brazil', 'mekong': 'vietnam'}

for river, country in famous_river.items():
    print(f"{river.title()} river runs through {country.title()}")

for river in famous_river.keys():
    print(river.title())

for country in famous_river.values():
    print(country.title())
print("\n")


#6-6 polling

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['jen', 'matt', 'rachel', 'jacon', 'phil']

for name in fav_languages.keys():
    if name in friends: 
        friends = fav_languages[name].title()
        print(f"Thank you {name.title()} for taking the poll")
    else: 
        print(f"{name.title()}, please take the poll")