try:
    num = int(input("Enter the number : "))
    print(f"Number entered is {num}")
except Exception as e:   # here the original Exception that occured a/c to python is stored in 'e'
    print(e)



try:
   num2 = int(input("Enter the number again: ")) 
   print(f"Number entered is {num2}")
except:                 # here when any type exception occured then the print statement of except block will execute
    print("Invalid input !")



try:
   Ind = [5,4,21]
   num3 = int(input("Enter the index to print : ")) 
   print(f"value at index {num3} is {Ind[num3]}")
except ValueError:  # this except block executes only when any exception related to Value occures like when any alphabet entered etc.             
   print("Number entered is not an integer.")
except IndexError:  # this except block executes only when any exception related to Index of 'Ind' array occures like out of range index etc.
    print("out of range index entered")
