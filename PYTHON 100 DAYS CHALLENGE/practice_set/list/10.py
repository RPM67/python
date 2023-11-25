# Python program to check if the list contains three consecutive common numbers in Python

input = [1, 1, 1, 64, 23, 5, 5, 5, 5, 64, 22, 22, 22]
print(len(input))
output = []
for i in range(1,len(input)-1):
    if input[i] == input[i-1] == input[i+1]:
        if input[i] not in output:
            output.append(input[i])

print(output)