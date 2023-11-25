class student:
    noOfStudents = 0 # this is class variable defined at the class level and is shared among all 
                     # instances or objects of the class.They are defined outside any method of
                     # class and are usually used to store information that is common to all instances
                     # of the class
    def __init__(self,name):
        self.name = name # instance variable, unique for every class  
        student.noOfStudents += 1
        
    def show(self):
        print(self.noOfStudents)
  
print(student.noOfStudents) # we can see here that the class variable is not bounded with any object
      
emp1 = student('rpm')
emp1.show()
emp2 = student('rpm')
emp2.show()
emp3 = student('rpm')
emp3.show()


