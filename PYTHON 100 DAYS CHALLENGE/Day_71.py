rt = [12,34,56]
print(dir(rt))# print all the available methods and attributes and everything that can be used on 'rt'

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.gender = 'M'
        
    def show(self):
        print(f"{self.name} - {self.age} - {self.gender}")
        
        
p1 = person('rpm',19)
print(p1.__dict__) # it will print all the attributes or variable created with self parameter inside the class then print those 
                   # attributes as dictionary items for this p1 object by
                   #  assinging the values of p1 for those attibutes if given.


help(person)# it will print all the description about the class 'person' along with their all methods.
