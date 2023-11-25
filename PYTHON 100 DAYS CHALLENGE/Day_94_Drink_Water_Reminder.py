from plyer import notification
import time
import win32com.client 
import os
speaker = win32com.client.Dispatch("SAPI.SpVoice")
user = input("Enter your Name : ")
interval = float(input("Enter the time interval(in hours) at which you want reminder : "))
minute = interval * 60
print(minute)
while True:
    for i in (range(1,int(minute))):
        os.system('cls')
        print(f"{(minute+1)-i} minutes left...") 
        time.sleep(i/i*60) 
    speaker.Speak(f"{user} you should drink water now")
    notification.notify(title="water",message="you should drink water",timeout=10)
    stop = input("Press Enter to continue or 'q' to quit: ").lower()
    if stop == 'q':
        break

