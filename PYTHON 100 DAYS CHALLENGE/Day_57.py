class details():
    name = None 
    age = None
    def descprtion(self): # self refers to the object on which this class method is called 
        print(f"My Name is {self.name} and I am {self.age} years old")
        
rpm = details()
rpm.name = "Rahul"
rpm.age = 20
rpm.descprtion()

ob = details()
ob.descprtion()