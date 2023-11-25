avg = lambda x,y : (x+y)/2 # here lambda has taken two aguments x,y and returned their average simply. for this we don't need to 
                           # create a function with name and then call it then print it.
print(avg(4,8))

def fun_args(cube,value):
    return  5 + cube(value) # here cube stores (lambda x : x**3) which returns cube of value. to understand read below 

print(fun_args(lambda x : x**3, 3)) # lets say we need a fun. which returns cube of number added with some number 5. for that we have 
                                    # write a cube fun. then call that cube fun. and store it in function returing cube added with
                                    # 5. for that thing we simply created a fun. named fun_args() which returns cube added with 5 then
                                    # took a cube function and value of which we want cube as argument in fun_args() and returned the
                                    # cube fn. added with 5. in print statement we passed whole cube fn. using lambda and the value 
                                    # of which we wanted the cube.  
                                    #  so lambda saved us from creating a cube fn then define it then send it to fun_args() etc. just
                                    # in 1 line. 
                                    # lambda mainly used as function argument like here in bigger programs 

x = lambda x, y: print(f'{x} * {y} = {x * y}')
print(x(4,5))
