# Given a list, write a Python program to swap first and last element of the list.

input = [12, 35, 9, 56, 24]

print(input)

temp = input[0]
input[0] = input[-1]
input[-1] = temp

print(input)




