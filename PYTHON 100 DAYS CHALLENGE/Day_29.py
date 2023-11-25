import this  # The Zen of python Guide Poem or EASTER EGG


def multiply(a,b):
    '''Takes in two numbers a,b and returns their multiplcation i.e axb'''
    return a*b

print("a x b : ",multiply(3,4))
print(multiply.__doc__)

def sum (a,b):
    x = a
    y = b
    '''Takes in two numbers a,b and returns their addition i.e a+b''' # python will treat it as
                                     # comments not docstring and returns 'none' because it is not 
                                     # written right after the function definition as written above
    return x*y
    

print("a x b : ",sum(3,4))
print(sum.__doc__)  

