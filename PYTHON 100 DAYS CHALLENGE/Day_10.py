var = input("enter : ")
print(var,type(var)) # we can see here that the input value is stored as str in variable 'var'

var2 = int(input("enter same value as above again : "))
print(var2,type(var2)) # we can see here that after typecasting input fn. into int,the same user input is stored as int in variable 'var2'

var3 = input("enter same value as above again once more : ")
print(int(var)+2,type(var)) # here only for the operation(+2), the var3 is typecasted into 'int' datatype but the 'var3' variable is still 'str' datatype