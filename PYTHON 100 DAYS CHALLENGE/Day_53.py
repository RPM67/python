lst = [2,5,3,8,6,12,9]

def cube(x): 
    return x**3
cubes = list(map(cube,lst)) # here map fn. will apply fn. cube() to each element of given list 'lst' and store the result in new list
                            # cubes here.since map returns a map object so we converted it to list and then stored in cube
print(cubes)
square = list(map(lambda x: x*x,lst)) # here we are doing the same thing i.e. the map fn. will takes each element of list 'lst' and
                                      # apply the square method we wrote using lambda fn. and stored it in a variable sqaure by 
                                      # converting it to list.here lambda helped us from writing a dedicated fn. of square like above.
print(square)



def even(x):
    return x%2==0
evens = list(filter(even,lst)) # here filter fn. will apply fn. even() to each element of given list 'lst' and store the result in 
                               # new list evens.filter will send each item of provided list 'lst' to provided fn. even() and then
                               # even() will check the number and returns true if the number is even and false if number is not even.
                               # if even() fn. returns 'true' for given number then the filter will include that number in list 
                               # otherwise not. since filter returns a filter object so we converted it to list and then stored in
                               # evens variable as list
print(evens)
odds = list(filter(lambda x: x % 2 != 0,lst)) # here we are doing the same thing i.e. the filter fn. will takes each element of list
                                      # 'lst' and check if number is satifying the odd no. check method we wrote using lambda fn. and
                                      # if the lambda fn. return true value for that number then filter stored it in a variable odd
                                      # by converting it to list.here lambda helped us from writing a dedicated fn. of odd no. check
                                      #  like above.
print(odds)


from functools import reduce # since reduce is not a built-in module, so we have to import it from functools library

def sum(x,y): 
    return x+y
sums = reduce(sum,lst) # here reduce fn. will take 1st two values from provided list i.e. 2,5 here and send it to provided fn. sum()
                       # which returns the ad of these two numbers. now reduce will store the sum i.e. 7 here and now send the result
                       # along with the next number i.e. 3 here to sum() fn. again which will give sum of the given two no. i.e 7 and
                       # 3 and send their sum i.e 10 to reduce fn. and reduce will again send this result along with next number to
                       # provide fn. until a final result came from sum() fn. and will store it to variable 'sums' and will print it.
print(sums)
sums2 = reduce(lambda x,y: x*y, lst)
print(sums2)