a = [3,5,2,9]
b = [3,5,2,9]

print(a is b) # lists are mutable objects and when created using different variables, they takes different location in memory and 
              # is not exact same object in memory so it will return false.
print(a==b) # since both lists have same value, so it will return true


a = 4
b = 4
print(a is b)# integers,tuples,strings.. all these are immutable objects in python and their value cannot be changed in memory. so,
            # python will assign only single memory unit for storing them and whenver another variable is storing same value then 
            # python will point those variable to that same memory unit where that value is stored and will not assign another memory
            # unit to different different variables that stores that same immutable object i.e a and b will be assigned same memory
            # unit here because they are string same immutable object i.e. integer whose value cannot be change. since 3 will remain
            # 3 for all variables and its value cannot be changed, so all variable will be pointed to same memory unit that is storing
            # the integer 3
print(a==b) # since both lists have same value, so it will return true


a = "harry"
b = "harry"
print(a is b) # since string is also an immutable object so....
print(a == b) # since both lists have same value, so it will return true


a = (2,5,7)
b = (2,5,7)
print(a is b) # since tuples is also an immutable object so....
print(a == b) # since both lists have same value, so it will return true