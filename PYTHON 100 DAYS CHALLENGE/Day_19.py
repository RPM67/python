for i in range(10):
    if(i==8):
        print("loop exited due to break")
        break
    print(i)

print("\n")

for i in range(10):
    if(i==7):
        print("iteration skipped due to continue")
        continue
    print(i)
