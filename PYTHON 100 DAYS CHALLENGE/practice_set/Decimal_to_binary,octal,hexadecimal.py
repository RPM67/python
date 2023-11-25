dec = int(input("Enter the number : "))

binary = bin(dec)
octal = oct(dec)
hexadecimal = hex(dec)

print("The binary value of ",dec,"is : ", end="")
for i in range(2,len(binary)):
    print(binary[i],end="")
print("\n")

print("The octal value of ",dec,"is : ", end="")    
for i in range(2,len(octal)):
    print(octal[i],end="")
print("\n")

print("The hexadecimal value of ",dec,"is : ", end="")
for i in range(2,len(hexadecimal)):
    print(hexadecimal[i],end="")        
print("\n")