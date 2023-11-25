# Create a program capable of displaying questions to the user like KBC. Use List data type to store
# the questions and their correct answers. Display the final amount the person is taking home after
# playing the game.

import time
print("\n\t\t Welcome to Kaun Banega Karore Pati\n")
contestantName = input("Enter Your Name Here : ")
print("\nHello",contestantName," Please Choose One Option From Below :- \n")
print("A - Start The Game\nB - Show Me The Price Pool\nC - Show Me The Game Rules\nD - Exit The Game")
def choice():
    choice = input("Enter Your Choice : ")
    return choice
def user_answer():
    answer = input("Answer : ")
    return answer
final_amount = 0
def Game():
    choicee = choice()
    match choicee:
     case 'A':
        print("\nHello",contestantName,"We hope that you read all the game rules above and now here to play the game")
        print("\nThe Questions will appear in few seconds")
        print("\nBest of Luck\n")
        time.sleep(6)

        # Question 1.
        Question_1 = ["Q.1. What is the maximum length of a Python identifier?","32","16","128","no fixed length"]
        print(Question_1[0],"\n","\t1.",Question_1[1],"\t2.",Question_1[2],"\t3.",Question_1[3],"\t4.",Question_1[4])
        
        def ans1():
            final_amount = 0
            uA = user_answer()
            if (uA == "4"):
                print("\nCongratulations You Won ₹1,000/-\n")
                final_amount = 1000

            elif (uA == "1" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_1[4])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again")
                exit() 
            else:
                print("Please Enter a choice from above given options")
                ans1()
        ans1()


        # Question 2.
        time.sleep(1)
        Question_2 = ["Q.2. What will be the output of the following code snippet?\n\tprint(2**3 + (5 + 6)**(1 + 1))","129","8","121","None"]
        print(Question_2[0],"\n","\t1.",Question_2[1],"\t2.",Question_2[2],"\t3.",Question_2[3],"\t4.",Question_2[4])
        
        def ans2():
            final_amount = 1000
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹2,000/-\n")
                final_amount = 2000

            elif (uA == "4" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_2[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans2()
        ans2()


        # Question 3.
        time.sleep(1)
        Question_3 = ["Q.3. How is a code block indicated in Python?","Brackets","Indentation","Key","None"]
        print(Question_3[0],"\n","\t1.",Question_3[1],"\t2.",Question_3[2],"\t3.",Question_3[3],"\t4.",Question_3[4])
        
        def ans3():
            final_amount = 1000
            uA = user_answer()
            if (uA == "2"):
                print("\nCongratulations You Won ₹3,000/-\n")
                final_amount = 3000

            elif (uA == "4" or uA == "1" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_3[2])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again")
                exit() 
            else:
                print("Please Enter a choice from above given options")
                ans3()
        ans3()


        # Question 4.
        time.sleep(1)
        Question_4 = ["Q.4. Which of the following concepts is not a part of Python?","Pointers","Loops","Dynamic Typing","All Of The Above"]
        print(Question_4[0],"\n","\t1.",Question_4[1],"\t2.",Question_4[2],"\t3.",Question_4[3],"\t4.",Question_4[4])
        
        def ans4():
            final_amount = 1000
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹5,000/-\n")
                final_amount = 5000

            elif (uA == "4" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_4[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans4()
        ans4()


        # Question 5.
        time.sleep(1)
        Question_5 = ["Q.5. Which of the following statements are used in Exception Handling in Python?","try","Except","Finally","All Of The Above"]
        print(Question_5[0],"\n","\t1.",Question_5[1],"\t2.",Question_5[2],"\t3.",Question_5[3],"\t4.",Question_5[4])
        
        def ans5():
            final_amount = 1000
            uA = user_answer()
            if (uA == "4"):
                print("\nCongratulations You Won ₹10,000/-\n")
                final_amount = "₹10,000/-"

            elif (uA == "1" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_5[4])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans5()
        ans5()


        # Question 6.
        time.sleep(1)
        Question_6 = ["Q.6.Which of the following types of loops are not supported in Python?","for","while","do-while","None"]
        print(Question_6[0],"\n","\t1.",Question_6[1],"\t2.",Question_6[2],"\t3.",Question_6[3],"\t4.",Question_6[4])
        
        def ans6():
            final_amount = "₹10,000/-"
            uA = user_answer()
            if (uA == "3"):
                print("\nCongratulations You Won ₹20,000/-\n")
                final_amount = "₹20,000/-"

            elif (uA == "1" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_6[3])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans6()
        ans6()


        # Question 7.
        time.sleep(1)
        Question_7 = ["Q.7.Which of the following is the proper syntax to check if a particular element is present in a list?","if ele in list","if not ele not in list","Both 1 and 2","None"]
        print(Question_7[0],"\n","\t1.",Question_7[1],"\t2.",Question_7[2],"\t3.",Question_7[3],"\t4.",Question_7[4])
        
        def ans7():
            final_amount = "₹10,000/-"
            uA = user_answer()
            if (uA == "3"):
                print("\nCongratulations You Won ₹40,000/-\n")
                final_amount = "₹40,000/-"

            elif (uA == "1" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_7[3])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans7()
        ans7()


        # Question 8.
        time.sleep(1)
        Question_8 = ["Q.8.Which of the following functions converts date to corresponding time in Python?","strptime()","strftime()","Both 1 and 2","None"]
        print(Question_8[0],"\n","\t1.",Question_8[1],"\t2.",Question_8[2],"\t3.",Question_8[3],"\t4.",Question_8[4])
        
        def ans8():
            final_amount = "₹10,000/-"
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹80,000/-\n")
                final_amount = "₹80,000/-"

            elif (uA == "3" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_8[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans8()
        ans8()


        # Question 9.
        time.sleep(1)
        Question_9 = ["Q.9.Which of the following blocks will always be executed whether an exception is encountered or not in a program?","try","Except","Finally","None"]
        print(Question_9[0],"\n","\t1.",Question_9[1],"\t2.",Question_9[2],"\t3.",Question_9[3],"\t4.",Question_9[4])
        
        def ans9():
            final_amount = "₹10,000/-"
            uA = user_answer()
            if (uA == "3"):
                print("\nCongratulations You Won ₹1,60,000/-\n")
                final_amount = "₹1,60,000/-"

            elif (uA == "1" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_9[3])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans9()
        ans9()


        # Question 10.
        time.sleep(1)
        Question_10 = ["Q.10.What keyword is used in Python to raise exceptions?","raise","try","goto","Except"]
        print(Question_10[0],"\n","\t1.",Question_10[1],"\t2.",Question_10[2],"\t3.",Question_10[3],"\t4.",Question_10[4])
        
        def ans10():
            final_amount = "₹10,000/-"
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹3,20,000/-\n")
                final_amount = "₹3,20,000/-"

            elif (uA == "3" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_10[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans10()
        ans10()



        # Question 11.
        time.sleep(1)
        Question_11 = ["Q.11.Which of the following is not a valid set operation in python?","union","intersection","difference","None"]
        print(Question_11[0],"\n","\t1.",Question_11[1],"\t2.",Question_11[2],"\t3.",Question_11[3],"\t4.",Question_11[4])
        
        def ans11():
            final_amount = "₹3,20,000/-"
            uA = user_answer()
            if (uA == "4"):
                print("\nCongratulations You Won ₹6,40,000/-\n")
                final_amount = "₹6,40,000/-"

            elif (uA == "1" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_11[4])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans11()
        ans11()


        # Question 12.
        time.sleep(1)
        Question_12 = ["Q.12.Which of the following are valid escape sequences in Python?","\\n","\\t","\\\\","All Of The Above"]
        print(Question_12[0],"\n","\t1.",Question_12[1],"\t2.",Question_12[2],"\t3.",Question_12[3],"\t4.",Question_12[4])
        
        def ans12():
            final_amount = "₹3,20,000/-"
            uA = user_answer()
            if (uA == "4"):
                print("\nCongratulations You Won ₹12,50,000/-\n")
                final_amount = "₹12,50,000/-"

            elif (uA == "1" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_12[4])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans12()
        ans12()


        # Question 13.
        time.sleep(1)
        Question_13 = ["Q.13.Which of the following modules need to be imported to handle date time computations in Python?","datetime","date","time","timedate"]
        print(Question_13[0],"\n","\t1.",Question_13[1],"\t2.",Question_13[2],"\t3.",Question_13[3],"\t4.",Question_13[4])
        
        def ans13():
            final_amount = "₹3,20,000/-"
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹25,00,000/-\n")
                final_amount = "₹25,00,000/-"

            elif (uA == "3" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_13[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans13()
        ans13()


       # Question 14.
        time.sleep(1)
        Question_14 = ["Q.14.How can assertions be disabled in Python?","passing -O when running python","Assertions are disabled by default","Both 1 and 2","Assertion cannot be disabled in python"]
        print(Question_14[0],"\n","\t1.",Question_14[1],"\t2.",Question_14[2],"\t3.",Question_14[3],"\t4.",Question_14[4])
        
        def ans14():
            final_amount = "₹3,20,000/-"
            uA = user_answer()
            if (uA == "1"):
                print("\nCongratulations You Won ₹50,00,000/-\n")
                final_amount = "₹50,00,000/-"

            elif (uA == "3" or uA == "2" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_14[1])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans14()
        ans14()


        # Question 15.
        time.sleep(1)
        Question_15 = ["Q.15.Which of the following are valid string manipulation functions in Python?","count()","upper()","strip()","All Of The Above"]
        print(Question_15[0],"\n","\t1.",Question_15[1],"\t2.",Question_15[2],"\t3.",Question_15[3],"\t4.",Question_15[4])
        
        def ans15():
            final_amount = "₹3,20,000/-"
            uA = user_answer()
            if (uA == "4"):
                print("\nCongratulations You Won ₹75,00,000/-\n")
                final_amount = "₹75,00,000/-"

            elif (uA == "1" or uA == "2" or uA == "3"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_15[4])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans15()
        ans15()


        # Question 16.
        time.sleep(1)
        Question_16 = ["Q.16.As what datatype are the *args stored, when passed into a function?","List","Tuple","Dictionary","None"]
        print(Question_16[0],"\n","\t1.",Question_16[1],"\t2.",Question_16[2],"\t3.",Question_16[3],"\t4.",Question_16[4])
        
        def ans16():
            final_amount = "₹75,00,000/-"
            uA = user_answer()
            if (uA == "2"):
                print("\nCongratulations You Won ₹1 crore/-\n")
                final_amount = "₹75,00,000/-"

            elif (uA == "1" or uA == "3" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_16[3])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans16()
        ans16()


        # Question 17.
        time.sleep(1)
        Question_17 = ["Q.17.In which language is Python written?","C++","C","Java","None"]
        print(Question_17[0],"\n","\t1.",Question_17[1],"\t2.",Question_17[2],"\t3.",Question_17[3],"\t4.",Question_17[4])
        
        def ans17():
            final_amount = "₹75,00,000/-"
            uA = user_answer()
            if (uA == "2"):
                print("\nCongratulations You Won The Grand Price ₹7 crore/-\n")
                final_amount = "₹7 crore/-"
                print("\t\tVery well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Us Again") 

            elif (uA == "1" or uA == "3" or uA == "4"):
                print("Sorry Wrong Answer")
                print("The correct answer is",Question_17[2])
                print("Very well played, Final Amount You Won : ",final_amount,"\nThank You For Playing Our Game.\n\tPlease Visit Again") 
                exit()
            else:
                print("Please Enter a choice from above given options")
                ans17()
        ans17()


        

     case 'B':
        print("\nFor Every Correct Answer You Will Get The Price Listed Below In Front Of Every Question Number :")
        print("\nThe Price Pool is As Following :-\n")
        price_list = ["₹1,000/-\n", "₹2,000/-","₹3,000/-", "₹5,000/-","₹10,000/-","₹20,000/-","₹40,000/-","₹80,000/-","₹1,60,000/-","₹3,20,000/-","₹6,40,000/-","₹12,50,000/-","₹25,00,000/-","₹50,00,000/-","₹75,00,000/-", "₹1 Crore/-", "₹7.5 Crore/-"]
        price_list.reverse()
        count = 17
        for i in price_list:
            print("Question ",count,":",i)
            count -= 1
        Game()    
     case 'C':
        print("\nThe Game Price Rules are as follows :-\n")
        print("1. if your answer is wrong  from Question Number 2 to 5 then you will get ₹1000/- only")
        print("2. if your answer is wrong  from Question Number 6 to 10 then you will get ₹10,000/- only")
        print("3. if your answer is wrong from Question Number 11 to 15 then you will get ₹3,20,000/- only")
        print("4. if your answer is wrong in Question Number 16 and 17 then you will get ₹75,00,000/- only\n")
        Game()
     case 'D':
        print("Thank You For Playing Our Game.\n\tPlease Visit Again")
        exit()
        Game()
     case _:
        print("Please Enter a Correct Choice Given Above")  
        Game()    

Game()






