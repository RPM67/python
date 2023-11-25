for i in range(5):
    print(f"iteration {i} completed successfully")
else:
    print("sorry,all iterations completed")

for i in range(5):
    if (i==2):
        continue
    print(i)
else:
     print("sorry,all iterations completed") # due to contnue only 1 iteration gets skipped bot loop completed, so else part executed
    

for i in range(5):
    if (i==2):
        break
    print(i)
else:
     print("sorry,all iterations completed") # due to break the loop did not completed, so else part not not executed
    

i = 0
while i < 7:
    print(i,end="\t")
    i+=1
else:
    print("iterations finished")