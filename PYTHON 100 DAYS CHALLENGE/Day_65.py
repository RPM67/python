class roots:
    @staticmethod # by using 'staticmethod' decorator, any method written in its indentation will be a static method. they don't have
                  # any access to instance or object of the clas due to which they can be used without creating any object of this 
                  # class on other variables too.
                  #  
    def square(a): # it is the only method of the class which can be created without using self parameter
        return a*a

    def cube(a):
        return a*a*a
    
result = roots.square(5)
print(result)

rts = roots()
print(rts.square(4))