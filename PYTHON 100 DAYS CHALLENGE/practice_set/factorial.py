#Find the Factorial of a given Number

num = int(input("Enter a number : "))
fact = 1
if(num<0):
    print("please enter a positive integer") 
elif(num == 1 or num == 0):
    print("factorial of",num,"is",1)   
else:
    for i in range(1,num+1):
        fact = fact*i
    print("factorial of",num,"is",fact)
    
