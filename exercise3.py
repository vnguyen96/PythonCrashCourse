#4-11 pg 114 

pizzas = ['sausage', 'peporoni', 'bacon']

for pizza in pizzas:
    print(f"I like {pizza}")

print ("I really like pizza!")



friends_pizzas = pizzas [:]

pizzas.append('hawaii')
friends_pizzas.append('cheese')

for pizza in pizzas:
    print(f"My fav pizzas are {pizza}")

for pizza in friends_pizzas:
    print(f"My friend's fav pizzas are {pizza}")