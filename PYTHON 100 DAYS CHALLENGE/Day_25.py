color = ("red","blue","green","yellow")

temp = list(color) # "converting tuple to list", a copy of tuple "color" converted to list is stored
                   #   in "temp"
print(type(color),color)
print(type(temp),temp)
temp.append("black")    # add item 
temp.pop(3)             # remove item 
temp[1] = "pink"        # change item
color = tuple(temp) # "converting list to tuple"
print(type(temp),temp)
print(type(color),color) 

num = (1,5,7,3,9,5,3,9,21,5)
res = num.count(5)
print("5 is repeated",res,"times in tuple")

num = (1,5,7,3,5,0,3,9,21,5)
res = num.index(3)
print('First occurrence of 3 in tuple is at index', res)
res = num.index(5,2,7)
print('First occurrence of 5 in tuple is at index', res) # the element 5 will be searched b/w index
                                                         # 2 to 6(7-1=6)
