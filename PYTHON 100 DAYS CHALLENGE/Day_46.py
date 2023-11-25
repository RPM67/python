import os


try:
    os.mkdir("Testing Day 46 Code")# this will create a folder of 'given name' in same directory this file
                                   # is present. if folder/file already exist then gives error too.
                                   # to do operations on any other location just open that location here
                                   #  by drag'n drop or by using 'open with' 
except FileExistsError: 
    print("file already exist")


try:
    f = os.open("Testing Day 46 Code/file.txt",os.O_RDWR)# file opened for read-write mode.search google for many other functions
    data = os.read(f,1024)# stores the content inside the file into 'data' variable
    print(f"\n{data}")
    os.write(f, b"Hello, world!")# Write to the file. delete the content you wanna write from actual file.txt before running for result
    print(data)
except FileNotFoundError:
    print("file is not found at given location")
finally:
    os.close(f)


files = os.listdir(".") # Get a list of the files in the current directory
print(files)
files2 = os.listdir("Testing Day 46 Code") # Get a list of the files in the given directory
print(files2)


output = os.system("ls") # Run the "ls" command and print the output
print(output)


f = os.popen("ls")
output = f.read()
print(output)
f.close()