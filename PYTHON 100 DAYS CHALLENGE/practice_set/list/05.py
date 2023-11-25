# Python program to count positive and negative numbers in a list

input = [2, -7, 5, -64, -14,0,23,45,-32,78,12,6]
print("The original list is : ",input)
pos = 0
neg = 0
zeros = 0
for i in input:
    if i>0:
        pos += 1
    elif i==0:
        zeros += 1
    else:
        neg += 1

print("total positive no. in list : ",pos)
print("total zeros in list : ",zeros)
print("total negative no. in list : ",neg)


