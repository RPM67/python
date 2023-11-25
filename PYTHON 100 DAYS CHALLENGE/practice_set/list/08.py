# How to count unique values inside a list

input =  [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print("The original list is : ",input)

output = []

for i in input:
   if input.count(i)==1:
      output.append(i)

print("Unique values inside list is : ",output)