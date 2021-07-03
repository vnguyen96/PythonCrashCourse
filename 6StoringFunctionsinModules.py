#Import an Entire Module

    #Import make_pizzas.py module

import make_pizzas

make_pizzas.make_pizza(16, 'popperoni')
make_pizzas.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#Import Specific Function

from make_pizzas import make_pizza

make_pizza(16, 'popperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#Using as to Give a Function an Alias 

from make_pizzas import make_pizza as mp

mp(16, 'popperoni')
mp(12, 'mushroom', 'green peppers', 'extra cheese')

#Using as to Give a Module an Alias

import make_pizzas as mp

make_pizza(16, 'popperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#Import All Functions in a Module

from make_pizzas import * #'***** it's best not to use this****

make_pizza(16, 'popperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
