# Remove multiple elements from a list in Python

input = [12, 67, 98, 34]
print("The original list is : ",input)

for i in input:
    if i%2==0:
        input.remove(i)

print(input)