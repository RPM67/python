class person:
    def __init__(self, value): # here we have initialised a '._health' property for the object which will be initialised automatically
                               # and set the value for ._health property of object automatically for every object of this class
        self._health = value

    
    def show(self): # we need to run this method to print the value of '._health' property of every object of this class 
        print(self._health)
    
    @property
    def life(self): # by using this life getter we can print the value of '._health' property of each object of this class 
                      # as an attribute of the class 
        return self._health

    @life.setter # using this setter we can change the value '._health' property of the object of this class multiple times without
                   # changing the initial parameter provided for '._health' property at object intialisation mutiple times in program directly
    def life(self, new_health_value):
        self._health = new_health_value

        
rpm = person(100)
# obj.show()
print(rpm.life) 
rpm.life = 70
print(rpm.life)

rpm.life = 90
print(rpm.life)