class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"The age of {self.name} is {self.age}")
      
    @classmethod
    def from_string(cls,string): # it will take class as cls and person 1 name and age value stored in single variable as string 
                                # parameter
        name,age = string.split(',') # it will seperate the name and age parameter seperated by comma and store in name,age variable
        return cls(name,int(age)) # it will return an instance of class person with seperated name and age parameter which was 
                                  # initially stored in 1 single string
    
    
p1 = person.from_string('rpm,19') # here person(name,age) will be stored which was returned by classmethod called in p1 which will
                                  # create an object  'p1' of class person 
p1.show() # now we can normally use these type of methods for this object like other object methods normally 

# so basically here, we have created the object for class person even the name and age value is not seperated and stored in single 
# string by the help of class method as constructors