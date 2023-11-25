class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
class Circle(shape): # here Circle class inherits the shape class, and overrides the area() method.. The new implementation of the
                     # area method calculates the area of a circle, based on its radius. we have redefined this class circle here
                     # so that it can print area of circle using the class shape. this method in the circle class is said to 
                   # override the method in the shape class. When you create an instance of the derived class and call the overridden
                     # method area(), the version of the method area() in the derived class is executed, rather than the version of
                     # area() in the base class
                     
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
        
    def area(self):
        return 3.14 * super().area()

class Cube(shape): # from shape class into cube class, area method is overridden here to print the area of the cube 
    def __init__(self,l,b,h):
        self.l = l
        super().__init__(b,h)
    
    def area(self):
        return self.l * super().area()

class Cylinder(shape):
    def __init__(self,r,h):
        self.h = h
        super().__init__(r,r)
        
    def volume(self):
        return 3.14 * super().area() * self.h
  
rectangle = shape(5,9)
print("area of rectangle : ",rectangle.area())

circle = Circle(5)
print("area of circle : ",circle.area())

cube = Cube(2,5,9)
print("area of cube : ",cube.area())

cylinder = Cylinder(7,4)
print("volume of Cylinder : ",cylinder.area())

