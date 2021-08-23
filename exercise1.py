#9-1 Restaurant

class Restaurant:
    def __init__(self, restaurant_name, crusine_type):
        self.restaurant_name = restaurant_name
        self.crusine_type = crusine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Restaurant crusine is {self.crusine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant('PhoKing', 'Vietnamese')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant('La Toteca', 'Mexican')

restaurant_two.describe_restaurant()

restaurant_three = Restaurant('Mama Roma', 'Italian')

restaurant_three.describe_restaurant()


#9-3

class User:
    def __init__(self, first_name, last_name, age, position, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.location = location

    def describe_user(self):
        print(f"\nUser first name is {self.first_name.title()}.")
        print(f"User last name is {self.last_name.title()}.")
        print(f"User is {self.age} years old.")
        print(f"User is a {self.position}.")
        print(f"User is located at {self.location} facility.")

    def greeting_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")


user_one = User('vinh', 'nguyen', '24', 'NOC Tech', 'GB')
user_one.describe_user()
user_one.greeting_user()

user_one = User('dan', 'schupple', '31', 'NOC Manager', 'GB')
user_one.describe_user()
user_one.greeting_user()
hello 