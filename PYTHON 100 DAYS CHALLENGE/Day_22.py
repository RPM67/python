list = ["RPM","Chhaggan",3,21,True,"rahul"]
print(list)

print(list[1],list[4])
print(list[-3]) # len(list) - 3 = 5-3 = 2

print(list[1:])
print(list[:4]) # index 4 excluded
print(list[2:5]) # index 5 excluded

print(list[::2]) # takes whole list to operate as we left start and end index empty. it takes 1st
                   # index and from 1st it print every 2nd element only and leave other elements.

print(list[1:5:2]) # list sliced from index 1 to 4. 1st index printed then every 2nd index i.e 1,3,5.... within sliced index

if 21 in list:
    print("present")
else:
    print("not present")

lst_comprhnsn = [i for i in range(10) if i%2==0] # i is a variable here. you can use any other keyword also
print(lst_comprhnsn)

names = ["Sarah","Milo", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [items for items in names if "o" in items] # iteams is a variable here. you can use any other keyword also
print(namesWith_O)
namesWithh_O = [items for items in names[1:3] if "o" in items]
print(namesWithh_O)


