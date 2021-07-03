#8-12 pg 452
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients: ")

    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('bread', 'ham', 'cheese')
make_sandwich('bread', 'chicken', 'spinach')
make_sandwich('bread', 'meatball')

#8-13 User Profile

def build_profile(first, last, **user_info): 
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('vinh', 'last', location = 'crofton', work = 'skyline')
print(user_profile)


#8-14 Cars

def build_car(manufacture, model, **car_info):
    car_info['car_manufacture'] = manufacture
    car_info['car_model'] = model
    return car_info

car_profile = build_car('toyota', 'camry', color = 'white', miles = '20000')
print(car_profile)