def factoorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factoorial(n-1)
    
num = int(input("number : "))
print("Factorial : ",factoorial(num))

def fibbonacci(n):
    if (n<=0):
      print("enter a positive number")
    elif (n==1):
        return 0
    elif (n==2):
        return 1
    else:
        return (fibbonacci(n-1)+fibbonacci(n-2))
    
num2 = int(input("Enter position of fibbonacci: "))
fib = fibbonacci(num2)
print("fibbonacci number at position",num2,"is :",fib)