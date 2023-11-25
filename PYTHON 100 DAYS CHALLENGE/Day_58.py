class person():
    def __init__(self):
        print("I am a person")
        
rpm = person() # when you remove self from the 'init' functions from class, an error will be occured
               # because here the object will itself pass as an argumnet to the constructor which is
               # stored in 'self' parameter b/c we know self refers to the object on which the class
               # method is called 

class details():
    def __init__(self,name,age): # here self refers to the object.e.g. for object 'x',  self = 'x'
        self.name = name # for object 'xyz', self.name = xyz.name
        self.age = age
    
    def descp(self):
        print(f"name - {self.name}\nage - {self.age}")
    def descp2(random): #here we can see that just like self,random is just a normal variable which stores objects as an argument here
        print(random.name)
def hello():
    rahul = details("Rahul",20)
    rahul.descp()
    rahul.descp2()
    
hello()
    
            

