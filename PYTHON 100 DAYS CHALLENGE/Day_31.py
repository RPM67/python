set1 = {2,4,5,76,2,43,12,12,5,22,2,3,4}
print(set) # repeated value excluded and iteams occured in random order

set2 = {}   # this is empty dictionary not empty set
print(type(set2)) 

set3 = set()    # now this is empty set 
print(type(set3))

count = 1
for item in set1:
    print("set iteam",count," : ",item)
    count+=1