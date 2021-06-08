#8-3 T-shirt 

def make_shirt(size, message):
    print(f"\nYour shirt size is {size} and a message that printed {message}")

make_shirt('medium', 'Hello World!') #Positional Arguments

make_shirt(size='medium', message='Hello World!') #Keyword Arguments

#8-4 Large Shirts

def make_shirt(size='large', message='I love Python'):
    print(f"\nYour shirt size is {size} and a message that printed {message}")

make_shirt()
make_shirt(size='medium')

make_shirt(size='small', message='I love JavaScript')

#8-5 Cities 

def describe_city(city, country='USA'):
    print(f"\n{city.title()} is in {country.title()}")

describe_city(city='NY')
describe_city(city='Baltimore')
describe_city(city='Paris', country='France')

