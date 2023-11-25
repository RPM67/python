class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def details(self):
        print(f"name of Employee is {self.name} with id {self.id}")
    
    
class EmployeeSkills(Employee):
    def __init__(self,lang):
        self.languageSkill = lang
        
    def show(self):
        print(f"{self.name} with Employee id {self.id} has programming skiils in {self.languageSkill}")
    
emp1 = Employee('rpm',101) # emp1 will have access to properties of class Employee only   
emp1.details()

emp2 = EmployeeSkills('python') # emp2 will have properties of class Employee as well as class EmployeeSkills
emp2.name = 'rahul'
emp2.id = 102
emp2.details()
emp2.show()