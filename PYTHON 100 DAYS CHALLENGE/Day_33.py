employees = {'001':'RPM','002':'Rohit','003':'Sarang'}
print(employees)

print(employees.get('001'))
print(employees['003'])

print(employees.get('age')) # prints None as age is not a key of dictionary
# print(employees['age'])  # throws Key Error as age is not a key of dictionary

print(employees.keys())

print(employees.values())

print(employees.items())

for keys,values in employees.items(): # since items() method stores two entities i.e keys and values, so we took 2 variables here 
    print(f"the key is {keys} and its value is {values}")

