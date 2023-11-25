# python program to find an armstrong number 

# 153 = 1*1*1 + 5*5*5 + 3*3*3
# 153 = 1 + 125 + 9
# 153 = 153
# so 153 is an armstrong number.
# this same concept applies for every number 

num = int(input("Enter a number : "))

sum = 0
temp = num

while(temp>0):
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp //= 10  # removes last digit i.e makes 153 = 15, 15 = 1, 1 = 0

if(sum == num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")