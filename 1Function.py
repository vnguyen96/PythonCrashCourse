def greet_user():
    """Display a simple greeting.""" #this is a 'docstring'. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs 
    print("Hello!")

greet_user()


#Passing information to a function 

def greet_user(username): #By adding 'username' here you allow the function to accept any value of 'username' you specify
    """Display a simple greeting.""" 
    print(f"Hello, {username.title()}!")

greet_user('vinh')

    #'username' in 'greet_user(username)' is an parameter. 'vinh' in greet_user('vinh') is an argument. An argument is a piece of information that's passed from a function call to a function



    