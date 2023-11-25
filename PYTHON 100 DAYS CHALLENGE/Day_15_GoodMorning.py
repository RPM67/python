import time

timestamp1 = time.strftime('%c, %H:%M:%S')
print(timestamp1)

timestamp2 = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H')) #time will be converted to int value from string by using int() typecast
   

if(hour<5 and hour>20):
    print("Good night Mr. Mishra.\nits \""+time.strftime('%A')+"\" night and the time is "+timestamp2+" right now")
elif(hour>=5 and hour<=11):
    print("Good Morning Mr. Mishra.\nits \""+time.strftime('%A')+"\" Morning and the time is "+timestamp2+" right now")
elif(hour>11 and hour<=16):
    print("Good AfterNoon Mr. Mishra.\nits \""+time.strftime('%A')+"\" Noon and the time is "+timestamp2+" right now")
else:
    print("Good Evening Mr. Mishra.\nits \""+time.strftime('%A')+"\" Evening and the time is "+timestamp2+" right now")
    
    