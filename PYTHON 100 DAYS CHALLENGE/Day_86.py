numbers = [2,5,4,7,4,12]
while((n := len(numbers)) > 0): # the length of the numbers list is assigned to the variable n using the Walrus Operator. The value 
                                # of n is then used in the condition of the while loop, so that the loop will continue to execute 
                                # until the numbers list is empty.
    print(numbers.pop())
    
    
    
names = ['rpm','rakesh','rohit','shubham']
if (name := input("Enter your name : ")) in names: # by walrus operator we can take input from user inside expressions also like this
    print("your name is present in list")
else:
    print("your name is not present in list") 
    


food_item = []
while (food := input("Enter Your Favourite Food : ")) != 'quit': # by walrus operator we can take input from user inside expressions 
                                                                 # also like this and it will take user input until quit is entered 
    food_item.append(food)
    
if (user := input("Enter 'yes' to print the list if food you entered : ")) != "yes":
    print("thank you come again!")
else:
    for i in food_item:
        print(i)
    
# It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.
    