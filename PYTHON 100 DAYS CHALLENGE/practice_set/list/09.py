# List product excluding duplicates

input =  [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print("The original list is : ",input)
output = []
product = 1
for i in input:
    if input.count(i)>1:
        if not i in output:
            output.append(i)
            
for i in output:
    product = product*i   

print("list product excludung duplicates : ",product)