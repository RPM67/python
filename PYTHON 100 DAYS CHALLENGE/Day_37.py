def fun(i):
    try:
        ind = [2,5,7,3,4]
        print(f"Value at index {i} is {ind[i]}")
        return 1
    except IndexError:
        print("Out of Index")
        return 0
    except ValueError:
        print("Number is not Iteger")
        return 1
    finally:
        print("I am always executed even after function returned") # this print statement executed even after the fun has returned a
                                                                   # value because it is written in finally block so this statement
                                                                   # will execute at any cost

print("here i will not execute because function returned")  # this print statement will not not execute because the function has 
                                                            # already returned a value and not in finally block too, so this statement
                                                            # is neglisible now.to execute this print statement wehave to write this
                                                            # in finally block 


x = fun(2)
print(f"function returned value is {x}") # value returned from fun() will be printed here
    
