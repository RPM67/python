age = int((input("Enter your age : ")))

if(age>18):
    print("Eligible for voting")
else:
    print("not eligible for voting")
print("out of the else block") #this will be printed weather statement true or false because it is out of the indentation of else block.    


if(age>18):
    print("you are an adult")
elif(age<18 and age>=14):
    print("you are a teenager")
else:
    print("you are a minor")        

if(age>18):
    if(age>=25):
        print("perfect age of marraige, you should marry now")
    elif(age<25 and age>=21):
        print("not a perfect age for marraige but still you can marry now")
    elif(age<21 and age>=18):
        print("you are mature but still not ready for marraige")
else:
    print("you are not eligible for nothing neither voting nor maraaige")  


