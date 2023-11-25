from math import sqrt

class Vector:
    def __init__(self,i=0,j=0,k=0):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self1,self2): # this builtin method helps to overload the '+' operator to add two instances of a class too.
        return Vector((self1.i + self2.i), (self1.j + self2.j), (self1.k + self2.k))
    
    def __sub__(self1,self2): # this builtin method helps to overload the '-' operator to add two instances of a class too.
        return Vector((self1.i - self2.i), (self1.j - self2.j), (self1.k - self2.k))
    
    def mag(self): # this is normal class method which returns the magnitude of a vector 
        return sqrt(self.i**2 + self.j**2 + self.k**2)
    
v1 = Vector(2,4,5)
print(v1)

v2 = Vector(3,6,8)
print(v2)

v3 = v1 + v2
print(v3)

v4 = v1 - v2 
print(v4)

v5 = Vector(2,3,6)
print(v5)
print(v5.mag())