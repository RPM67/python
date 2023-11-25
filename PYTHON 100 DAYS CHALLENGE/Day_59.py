def decorator(fx): # this function decorator have taken fun() function as argument and stored in fx and we have done some add-on
                   # onto fx() and returned the new modified_fun()
    def modified_fun():
        print("Hello Universe")
        fx()
        print("Hello Country")
    return modified_fun
    
@decorator  # using this, the initial function fun() has been converted into decorator fn. and since decorator is returning fn. 
            # modified_fun() so modified_fun() will be executed even if we call function fun()
            
def fun(): 
    print("Hello World")
    
#decorator(fun)()   # this line will also do the same thing as @decorator done above, instead of that use can use this too

fun() # initially this function was printing only hello world but by using decorators we have modified the same function and now 
      # modified_fun() has run instead of this function fun() only 
      


num1 = 10
num2 = 25   

def decorators(fun):
    def mod_fn(*args,**kwargs): # args will store the arguments(num1,num2) of add() as tuple and kwargs as key value pairs of dictionary
        print("the sum is : ",args[0]+args[1])
        fun(*args,**kwargs)
        print("the division is : ",args[1]/args[0])
    return mod_fn

@decorators
def add(a,b):
     print("the multiplication is : ",a*b)

#decorators(add)(num1,num2) # will do same thing as above decorators will do
add(num1,num2) # intially the add() fun. was printing the sum of num1 and num2 only but now using decorators it will print multiply
               # and division too and all of this is done without modyfying the original add() function