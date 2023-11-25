# JOINING SETS

# union() and update()
harry = {1,2,3,4,5}
rpm = {3,4,5,6,7,8}
union = harry.union(rpm)
print("set 1 : ",harry)
print("set 2 : ",rpm)
print("union : ",union) # union = set1 U set2

print("set 1 : ",harry)
harry.update(rpm)
print("set 1 : ",harry) # set1 = set1 U set2

print("\n")

# intersection() and intersection_update()
harry = {1,2,3,4,5}
rpm = {3,4,5,6,7,8}
intersection = harry.intersection(rpm)
print("set 1 : ",harry)
print("set 2 : ",rpm)
print("intersection : ",intersection) # intersection = set1 ∩ set2

print("set 1 : ",harry)
harry.intersection_update(rpm)
print("set 1 : ",harry) # set1 = set1 ∩ set2

print("\n")

# symmetric_difference() and symmetric_difference_update() 
harry = {1,2,3,4,5}
rpm = {3,4,5,6,7,8}
symmetric_difference = harry.symmetric_difference(rpm)
print("set 1 : ",harry)
print("set 2 : ",rpm)
print("symmetric difference : ",symmetric_difference) # symmetric_difference = (set1 U set2) - (set1 ∩ set2)

print("set 1 : ",harry)
harry.symmetric_difference_update(rpm)
print("set 1 : ",harry) # set1 = (set1 U set2) - (set1 ∩ set2)

print("\n")

# difference() and difference_update() 
harry = {1,2,3,4,5}
rpm = {3,4,5,6,7,8}
difference = harry.difference(rpm)
print("set 1 : ",harry)
print("set 2 : ",rpm)
print("difference : ",difference) # difference = set1 - (set1 ∩ set2)

print("set 1 : ",harry)
harry.difference_update(rpm)
print("set 1 : ",harry) # set1 = set1 - (set1 ∩ set2)

# SET METHODS

s1 = {1,3,5,8}
s2 = {6,7,10,3}
print("disjoint : ",s1.isdisjoint(s2))

sup = {2,4,6,8,90,34,51}
sub = {6,8,34}
print("superset :",sup.issuperset(sub))

sup = {2,4,6,8,90,34,51}
sub = {6,8,34}
print("superset :",sub.issubset(sup))



set = {2,4,7}

print(set)
set.add(5) 
print(set)

print(set)
tup = (1,8,9,3)
set.update(tup)
print(set)

print(set)
set.remove(8)
# set.remove(11)  # since 11 is not present in set, so executing this remove method will throw error
print(set)

print(set)
set.discard(9)
set.discard(11)  # since 11 is not present in set, but this discard method still executes
print(set)

print(set)
item = set.pop()
print(item)
print(set)

if 4 in set:
    print("present")
else:
    print("not present")

print(set)
set.clear() # set becomes empty here
print(set)    

s = {2,4,56}
print(s)
del s
#print(s) # will give not found error 