emp1 = { 101:'Rahul',102:'Rohit',103:'Raghav',104:'Ronit'}
print(emp1)
emp2 = { 105:'Aakash',106:'Akshay'}
emp1.update({103:'Suraj'})
print(emp1)
emp1.update(emp2)
print(emp1)


print(emp2)
emp2.clear()
print(emp2)


print(emp1)
emp1.pop(103)
print(emp1)


print(emp1)
emp1.popitem()
print(emp1)  # removes last key from dictionary


print(emp1)
del emp1[102]
print(emp1)

del emp1 # entire emp1 dictionary deleted 
# print(emp1)



