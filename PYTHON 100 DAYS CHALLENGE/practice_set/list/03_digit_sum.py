# Sum of number digits in List

input = [12, 67, 98, 34]
print("The original list is : ",input)

output = []
for i in input:
    sum = 0
    while i>0:
        digit = i % 10  # gives remainder after diving by 10 to a number. for 1st no. of list i.e. 12 the output will be 12/10 = "2"
        sum = sum + digit 
        i //= 10 # removes last digit i.e makes 112 = 11, 11 = 1, 1 = 0 (renoves digit from i which come after dividing by 10 here)
    output.append(sum)

print(output)

# in above example 