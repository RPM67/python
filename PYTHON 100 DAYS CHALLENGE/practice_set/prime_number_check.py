# prime number is a number which is not not divisible by any number except 1 and itself.
# e.g.  3,5,7,11,... is not divisible by any number except 1 and itself

num = int(input("Enter a number : "))

if (num==1):
    print(num,"is a not prime number")
if (num>1):
    for i in range(2,num):
        if(num%i == 0):
            print(num,"is a not prime number")
            break
        else:
            print(num,"is  a prime number")
            break

