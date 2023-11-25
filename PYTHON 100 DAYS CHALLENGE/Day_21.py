def num(a=0,b=0):      
    print("a+b :",a+b)

num()       # if defined arguments is not given above in function then we have to give both arguments here
num(1)
num(3,6)
num(b=2,a=5)  # we can swap orders of a and b but have to define it like here otherwise have to give arguments in same order   



def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("average is : ",sum/len(numbers))

avg(2,3,5,9,1,10) 



def sum(a,b,c):
    return a+b+c

c = sum(2,6,7)
print("sum is :",c)