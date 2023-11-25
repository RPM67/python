# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.

input = [0, 9, 5]

for i in range(len(input)):
    for j in range(len(input)):
        for k in range(len(input)):
            if (i!=j and j!=k and k!=i):
                print(input[i],input[j],input[k])

from itertools import permutations
per = 0
comb = permutations(input,len(input))
for i in comb:
    print(i) 
    per += 1

print(per)