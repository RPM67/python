class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.__salary = 10000 # An indication of private variable.by using '__' before variable name
    
    def show(self):
        print(f"name - {self.name}\nid - {self.id}")
    
    def __showSalary(self):  # An indication of private method. by using '__' before method name
        print(f"salary of {self.name} with id {self.id} is {self.__salary}")
        
emp1 = Employee('rpm',101)
print(emp1.name)
print(emp1.id)
#print(emp1.__salary) # it will throw error no attribute found because we cannot acess this class member directly outside like other 
                    # two because it is initialized as a private member inside class. see below how to access it outside class

emp1.show()

#emp1.__showSalary() # it will throw error no attribute found because we cannot acess this class method directly outside like other 
                    # one method because it is initialized as a private method inside class.see below how to access it outside class
                    
print(emp1._Employee__salary) # we can access the private member outside class like this by using the class name prefixed by single
                              # underscore (_) followed by private member name 
emp1._Employee__showSalary() # we can access the private method outside class like this by using the class name prefixed by single
                              # underscore (_) followed by private method name 
                              
# the main concept of using private and protected is to remind the coder and others that it should be used carefully and cannot get
# accessed or manipulated mistakenly. it does not provide any protection to the members or method and is a convention only