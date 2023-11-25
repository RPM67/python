class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def show(self):
        print(f"student - {self.name}\nroll - {self.roll}")
        
    def __str__(self): # when you print the object directly then this method will be invoked. if this method not defined then '--repr--'
                       # method will be invoked 
        return f"student - {self.name}\nroll - {self.roll}"
    
    def __repr__(self): # used to recreate the object.
        return f"student('{self.name}')"
    
    def __len__(self): # when you execute len() command on object then this method will be invoked 
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __call__(self): # when you use object directly as function call then this method will be invoked
        print("Hey I am good")
    
s1 = student('rpm',21667)
print(s1)
print(str(s1))
print(repr(s1))
print(len(s1))
s1()