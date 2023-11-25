# Program to print duplicates from a list of integers

input =  [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print("The original list is : ",input)
output = []
for i in input:
    if input.count(i)>1:
        if not i in output:
            output.append(i)

print("Duplicate values inside list is : ",output)