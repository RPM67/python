#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into 
#secret code language

# coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at
# the starting and the end else: simply reverse the string

# decoding
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last
# letter and append it to the beginning

# Your program should ask whether you want to code or decode


Id = "rpm"
Pass = "12345"
userId = input("Enter your Id : ")
if (userId != Id):
    raise PermissionError("Invalid User Name")
else:
    userPass = input("Enter your password : ")
    if(userPass != Pass):
        raise PermissionError("Unauthorised Access Attempted....Access Denied")
    else:
        print(f"\n\t\tHello {Id} Welcome to Your Secret Coding Decoding Platform\n")

print("Choose an Option From Below:-")
print("1. Coding \n2.Decoding")


def SecretCodng():
   try:
    choice = int(input("Your Choice : "))
    if(choice == 1):
        rndmKey1 = "qez"
        rndmKey2 = "avy"
        print("\t\tWelcome to Secret Messaege Coding Platform")
        message = input("Enter Your Message to Code : ")
        if(len(message)<3):
            temp = message[0]
            message[0] = message[1]
            message[1] = temp
            print(f"your message converted to secret code is : {message}")
        else:
            message = rndmKey1 + message[1:len(message)] + message[0] + rndmKey2 
            message = message.replace(" ","_")
            print(f"your message converted into secret code is : {message}")
    elif(choice == 2):
        print("\t\tWelcome to Secret Message Decoding Platform")
        message = input("Enter Your secret message code to decode it into message : ")
        if(len(message)<3):
            temp = message[0]
            message[0] = message[1]
            message[1] = temp
            print(f"your secret message code coverted into message is : {message}")
        else:
            message = message[len(message)-4] + message[3:len(message)-4]
            message = message.replace("_"," ")
            print(f"your secret message code coverted into message is : {message}")
    else:
        print("Enter a Valid Choice")
        SecretCodng()
   except ValueError:
       print("Enter a Valid Choice")
       SecretCodng()
       

SecretCodng()