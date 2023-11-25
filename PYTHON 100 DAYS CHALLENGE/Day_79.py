class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("The Animal Made Sound")
        
        
        
class Mammal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def make_sound(self):
        print("The Mammal Made Sound")
        
        
        
class Dog(Animal,Mammal): # here we inherited the class Animal,Mammal in class Dog
    def __init__(self,name,breed,color):
        Animal.__init__(self,name,species="Canis lupus familiaris")
        Mammal.__init__(self,name,color)
        self.breed = breed
    
    def make_sound(self): 
        print("Bark!")
    

dog = Dog("lucky","Llebrador","skin_color")
dog.make_sound()  # here python will firstly search for make_sound() method in class Dog and if not defined then will search the
                  # make_sound() method in the class inherited first in class Dog  i.e Animal here and if not found there also then
                  # will search in the next inherited class i.e. Mammal here and will go so on in all inherited method 1 by 1 to 
                  # search the method 
                
print(Dog.mro()) # it prints the order in which python gives preference for searching or doing any method. since Animal is written
                 # first then mammal class is written, so python will give Animal class more priority than Mammal class. if we 
                 # write Mammal class first then Animal class later, python will give Mammal class more priority than Animal class