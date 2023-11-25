import PyPDF2
import time
from roboSpeaker import commandSpeaker

# commandSpeaker("Welcome to pdf merger software by RPM. Here you can merge your multiple pdf files together as a single pdf file easily. lets go ")
print(
    "Welcome to pdf merger software by RPM.\nHere you can merge your multiple pdf files together as a single pdf easily.")
print("\nEnter the name of your pdf files below(e.g. sample.pdf... ) ")
#commandSpeaker("Enter the name of your pdf files below. Enter q to stop entering the files")
pdfFiles = []
def files_input():
    while True:
        user_input_files = input("Enter file name here : ('q' to stop entering files and 'ex' to exit program) : ").strip()
        if user_input_files == 'q':
            break
        elif user_input_files == 'ex':
            commandSpeaker("Thank You Please come again")
            exit("Thank You Please come again")
        if not user_input_files.endswith('.pdf'):
            print("Invalid File Name. Please try again")
            continue  # due to this the next lines of code in this loop will not execute without breaking the loop
        pdfFiles.append(user_input_files)


files_input()
def showFiles():
   # commandSpeaker("the list of your pdf files to merge are given below. The Merged Pdf file will also be in same sequence.")
    print("the list of your pdf files are given below :- ")
    for i in pdfFiles:
        print(i)


showFiles()
# commandSpeaker("enter yes below if wanna add more files in this list. otherwise no to proceed further with the same list above.")
while True:
    add_more_files = input("Wanna Add more pdf file in this list (yes/no or 'ex' to exit program) : ").strip()
    if add_more_files == 'yes':
        print()
        files_input()
        break
    elif add_more_files == 'no':
        break
    elif add_more_files == 'ex':
        commandSpeaker("Thank You Please come again")
        exit("Thank You Please come again")

showFiles()

commandSpeaker("merging your pdf files together")
print("merging your pdf files together.....")
time.sleep(2)
merger = PyPDF2.PdfMerger()  # PdfMerger() is like a list which takes the opened pdf files as input and in last merge them from top to bottom together as a single file
try:
    for file in pdfFiles:
        pdfFile = open(file, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(
            pdfReader)  # here the opened pdf file in 'pdfReader' variable is stored in the 'merger' list and every file opened after it will be appended in this merger list
        pdfFile.close()
    merger.write('merged.pdf')  # here the merged pdf file stored in merger list has been written or stored in new file
    print("your pdf file has been merged and saved as 'merged.pdf'. please check your file")
   # commandSpeaker("your pdf file has been merged and saved as 'merged.pdf'. please check your file")
except FileNotFoundError:
   # commandSpeaker("Some pdf files missing or maybe you entered a wrong file name. Please check your file and try again")
    print("Some pdf files missing or maybe you entered a wrong file name. Please check your file and try again")
except Exception as e:
    commandSpeaker("some problem occurred. please try again")
    print(f"some problem occurred. the problem is {e}. please try again!")
finally:
    time.sleep(2)
    commandSpeaker("Thank You Please come again")
    print("Thank You Please come again")