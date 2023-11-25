list = ["rpm","rohit"]
list.append("rakesh")
print(list)

num = [2,6,3,0,9,166,45,21,7,9,23,3,67,21,21,78]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

list.reverse()
print(list)

print(list.index("rohit"))

print(num.count(21)) # no. of times 21 is repeated in list

list_copy = list.copy() 
list_copy.append("mohit") # if list is directly taken instead of list.copy() then original list will be modified not list_copy
print(list)
print(list_copy)

print(list)
list.insert(1,"rahul")
print(list)

list1 = ["my","name","is"]
list2 = ["rahul","prakash","mshra"]
print(list1)
print(list2)
list1.extend(list2)
print(list1)

print(list1+list2)