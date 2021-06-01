#6-7 people 322

mylove = {'first_name': 'rachel', 'last_name': 'maasry', 'age': 26, 'city': 'crofton'}
myfriend = {'first_name': 'caleb', 'last_name': 'ruiz', 'age': 22, 'city': 'fairfax'}
mycousis = {'first_name': 'hy', 'last_name': 'tran', 'age': 20, 'city': 'gilbert'}

people = [mylove, myfriend, mycousis]

for person in people[:]:
    print(person)


#6-9 fav places

fav_places = {
    'rachel': ['lebanon', 'virginia'],
    'vinh': ['beach'],
    'becca': ['shore', 'annapolis'],
}

for person, places in fav_places.items():
    if len(places) <= 1:
        print(f"\n{person.title()} fav place is: ")
    else:
        print(f"\n{person.title()} fav places are: ")
    
    for place in places:
        print(f"\t{place.title()}")


#6-10 fav numbers

favorite_numbers = {
    'vinh': [11, 7, 69],
    'rachel': [1, 5, 9],
    'des': [23, 4, 6, 7],
    'matt': [5],
    'becca': [20, 22],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) <= 1:
        print(f"\n{person.title()} fav numer is")
    else:
        print(f"\n{person.title()} fav numbeers are")
    
    for number in numbers: 
        print(f"\t{number}")

#6-11 Cities 

cities = {
    'new york':{
        'country': 'usa',
        'population': 1000000.,
        'fact': 'it has good pizza!'
    },

    'saigon':{
        'country': 'vietnam',
        'population': 300000,
        'fact': 'it has great street food!'
    },

    'paris':{
        'country': 'france',
        'population': 500000,
        'fact': 'it has lovely people!'
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()} information are: ")

    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCity is located in {country.title()}")
    print(f"\tIt has the population of {population}")
    print(f"\tOne fun fact about this city is that {fact}")


