class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
        
    def show_details(self):
        print(f"name - {self.name}")
        print(f"species - {self.species}")
    
    
    
class Dog(Animal):
    def __init__(self,name,breed,color):
        Animal.__init__(self,name,species="Canis lupus familiaris")
        self.breed = breed
        self.color = color
    
    def show_details(self):
        Animal.show_details(self)
        print(f"breed - {self.breed}")
        print(f"color - {self.color}")
        
        
        
class GermanShephered(Dog): # this class inherits the Dog class and the Dog class inherits the Animal class
    def __init__(self,name,favFood):
        Dog.__init__(self,name,breed="German Shephered",color="mixture of black and brown")
        self.favFood = favFood
        
    def show_details(self): # this method uses the show_details() method of class Dog and the class Dog show_details() method will
                            # will use the show_details() method of class Animal. in this way multilevel inheritence implemented
        Dog.show_details(self)
        print(f"Favourite Food - {self.favFood}")

og = GermanShephered('Bahadur','meat')
og.show_details()   
        
        