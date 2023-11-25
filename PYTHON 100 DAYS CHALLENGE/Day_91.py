def my_generator():
    for i in range(5000000000):
        yield i # you can create a generator by using the yield statement in a function. The yield statement returns a value from
                # the generator and suspends the execution of the function until the next value is requested. it is helpful a lot
                # because normally we have to store the values in list and then reurn the values from that list which is hectic
                # in terms of memory and time if such bigger range of number is provided or lets say any complex operation have to
                # perform on some numbers but normally the complex operation will be done for all numbers which will cause memory
                # issues and take time too, so generators will help here by performing that complex operation on the number only 
                # when requested and not perform the operation on all the numbers. 
        
gen = my_generator()

print(next(gen)) # next() function is used to request the next value from the generator, and the generator resumes its execution 
                 # from previous value and returns a value from the generator  
print(next(gen))
print(next(gen))
print(next(gen))

# for j in gen: # it will simply print all the values by requesting the next values till the end
#     print(j)