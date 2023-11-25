x = int(input("Enter the value of x : "))

print("\t\tmatch case 1 :- ")

match x:
    case 0:
        print(0)
    case 10:
        print(10)
    case _ :
        print("default case")


print("\t\tmatch case 2 :- ")

match x:
    case 0:
        print("x is 0")
    case 10:
        print("x is 10")
    case _ if x<10:
        print("x is less than 10")
    case _ if x>10:
        print("x is greater than 10")      
