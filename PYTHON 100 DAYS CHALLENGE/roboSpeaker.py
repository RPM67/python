import win32com.client as wincom

if __name__ == "__main__":
    print("Welcome to the RoboSpeaker edition 1.1 Created by RPM")
    robo = wincom.Dispatch("SAPI.SpVoice")
    user = input('Enter your name : ')
    robo.Speak(f"hello {user}, hope you will be fine and having a good time. i am RoboSpeaker edition 1.1 Created by RPM. i am here to help you by converting anything that you enter below into voice command to help you to interact easily. Go Ahead, Enjoy!. and 1 more thing, if you wanna exit the program please enter the command 'quit' below")

    def roboSpeakUsingCommand():
        try:
            while True:
                command = input("Enter what you wanna say : ").lower()
                if command == 'quit':
                    break
                robo.Speak(command)
        except:
            print("Oops! Some error occurred")
            robo.Speak("Some unwanted error occurred. we will fix it and will come back to you again. Your coordination is appreciated")
        finally:
            robo.Speak(f"bye bye {user}. hope to see you again!")

    roboSpeakUsingCommand()
