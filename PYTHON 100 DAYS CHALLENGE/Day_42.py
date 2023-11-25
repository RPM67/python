marks = [54,68,87,61,91]

for ind,val in enumerate(marks):
    print(f"index {ind} : {val}")

print("\n")

for ind,val in enumerate(marks,start=2): # it will start the count from 2 not start taking value from 2nd index
    print(f"index {ind} : {val}")

