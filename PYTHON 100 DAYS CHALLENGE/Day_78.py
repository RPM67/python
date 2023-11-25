class Animal:
    def __init__(self,name):
        self.name = name
        
    def animal_sound(self):
        print("the animal make the sound")
        
    
class Cat(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name) # we have used single inheritence here and used this Animal class method here.
        self.color = color
       
    def animal_sound(self):  # in this Cat class, we redefined means override the animal_sound() method from Animal class to get
                             # precise value means sound of animal 
        print("Meow!")
    
    def animal_color(self):
        print("white")
        
    def animal_fav_food(self):
        print("milk")
    
    def animal_size(self):
        print("small, less than 2 feet normally") 
        
anml = Animal("dog") 
anml.animal_sound()

cat = Cat("kitty","white")  
cat.animal_sound()
cat.animal_color()
cat.animal_fav_food()  
        