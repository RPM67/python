class Employee:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def show(self):
        print(f"name - {self.name}\ncourse - {self.course}")
        
class Programmer(Employee):
    def __init__(self,name,course,lang):
        super().__init__(name,course) # since we are just adding the language and every thing is same as in parent class so we can 
                                      # super() keyword to use parent class methods here. here using super() we used the constructor
                                      # of parent class to assign the name and course of programmer by providing name and course in
                                      # the argument here. later, we assigned language of programmer using self parameter.
        self.language = lang
        
    def show(self):
        super().show()
        print(f"Preffered Programming Language : {self.language}")
        
p1 = Employee('rpm','BCA')
p1.show()

p2 = Programmer('rohan','MCA','python')
p2.show()