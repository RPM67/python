salary = int(input("Enter your salary : "))
if (salary<2000 or salary>10000):
    raise ValueError("Not a Valid Salary") # if user inputed salary doesn't fulfils condition then user will get this ValueEror with 
                                            # the message written inside the ValueError
else:
    print(f"your salary is {salary}")


Id = "rpm"
Pass = "12345"
userId = input("Enter your Id : ")
if (userId != Id):
    raise PermissionError("Invalid User Name")
else:
    userPass = input("Enter your password : ")
    if(userPass != Pass):
        raise PermissionError("Unauthorised Access Attempted....Access Denied")
    else:
        print("Hello Admin Welcome to your Base")