# Python program to get all unique combinations of two Lists

list_1 = ["a","b"]
list_2 = [1,2]
output = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        output.append((list_2[i],list_1[j]))

print(output)