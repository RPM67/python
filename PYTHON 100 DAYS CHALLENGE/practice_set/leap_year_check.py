# Python Program to Check Leap Year 

year = int(input("Enter a year : "))

if(year%4 == 0 and year%100 != 0): # condition for non centuries year like 2002,20003,2004....
    print(year,"is a leap year")
elif(year%100 == 0 and year%400 == 0): # # condition for centuries year like 2000,3000....
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")