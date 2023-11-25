from functools import lru_cache
import time

@lru_cache(maxsize=None) # this decorator will help in function caching here. for every unique input in the funtion fx(), the whole
                         # function will run for that input and then the result of that function for that input will be returned to
                         # function call and also the result that came after running the function for that input will be stored in
                         # function cache of this function. now the same process will be done for all unique inputs that came into 
                         # fx(). now, if any input for the function for which the function has already run, the python will not run
                         # the function again for that repeated same input and will return the result stored in cache of the fx() fun.
                         # that came after running the function for that repeated input directly to fun. call. it will save the fun.
                         # running time and resources for that input. the same thing will happen for every repeated value 
                         # here 'maxsize=None' means the function cache will have unlimited memory and you can set it also
def fx(n):
    print(f"performing opearations on {n}......")
    time.sleep(3)
    return f"result is {n**5}" # this return statement will be stored in cache of this function for every unique value and python
                               # will only return this return statement rather than running the function for that repeated value if
                               # the input for this function is repeated

while True:
    num = int(input("Enter the Number to Perform Operations on (1010 to exit) : "))
    if num == 1010:
        break
    print(fx(num))
    
    