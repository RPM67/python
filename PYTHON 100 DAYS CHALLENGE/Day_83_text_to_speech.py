# pip install pypiwin32 to install win32com.client module which convert text to speech in python

import win32com.client # 'win32com.client' is used to use microsoft speech engine in windows 

speaker = win32com.client.Dispatch("SAPI.SpVoice")

lst = ["Rahul","Aman","Anurag","Aditya"]

for name in lst:
    print(name)
    speaker.Speak(f"shoutout to {name} for using this course")
    

s = input("Enter the word you want to speak it out by computer : ")
speaker.Speak(s)