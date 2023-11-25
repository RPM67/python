tup = (1,4,"ram","rohit",6,32)
print(tup)

tup1 = (3)
print(tup1,type(tup1))
tup2 = (3,) #for single values in tuples we have to end it with a comma otherwise python will confused
print(tup1,type(tup2))

country = ("Spain", "Italy", "India", "England", "Germany")
print(country[3])
print(country[1])
print(country[-3]) #len(country)-3 = 2 , so 2nd index printed
print(country[-1]) #len(country)-1 = 4 , so 4th index printed

if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])   # from index 3 to 6(7-1)  
print(animals[-7:-2]) # from index len(animals)-7 = 9-7 = "2" to len(animals)-2 = 9-2 = "7" 

print(animals[:6])     # start index automatically taken 0
print(animals[:-3])    # from 0 to 9-3 = "6"

print(animals[4:])      # go till end of tuple starting from index 4
print(animals[-4:])     # go till end of tuple starting from index 9-4 = 5

print(animals[::2])# takes whole list to operate as we left start and end index empty. it takes 1st
                   # index and from 1st it print every 2nd element only and leave other elements.
                  
print(animals[1:8:3]) # list sliced from index 1 to 7. 1st index printed then every 3rd index printed
                      # within sliced index

print(animals[-8:-1:2]) # list sliced from index 9-8= "1" to 9-1= "8". 1st index printed then every 
                        # 2nd index printed within sliced index