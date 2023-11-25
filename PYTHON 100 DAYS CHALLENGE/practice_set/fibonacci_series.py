# python program to find a fibbonacci series sequence

# in fibonacci series the 1st 2 number are fixed i.e 0,1 and form 3rd onwards it is a sum of previous
# two numbers i.e for 3rd, it is sum of 1st and 2nd i.e 0+1 =1 , for 4th it is sum of 2nd and 3rd
# i.e 1+1=2, and so on 

num = int(input("Enter the value upto which you want to print the fibbonacci series : "))
a = 0
b = 1

if(num == 1):
    print(a)
elif(num < 1):
    print("please enter a valid number")
else:
    print("The fibbonacci series is : ",end="")
    print(a,b, end=" ")
    for i in range(2,num):
        c = a+b
        a = b
        b = c
        print(c, end=" ")