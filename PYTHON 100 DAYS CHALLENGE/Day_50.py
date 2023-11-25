f = open('Day 49 Code Test/myfile.txt', 'r') # file opened in only read mode
line = f.readline() # readline stored only one line from top in 'line' variable and in form of 'string'
print(line) 
print(type(line))

while True:
    line = f.readline() # line variable will get updated for each iteration of loop and prints the remaing lines which has been not 
                        # printed. see here for line 1 of file the iteration didn't run because line 1 of file already printed above 
    if not line:  # since loop is always True, so it will break the loop if line is not found after storing 1 line of file in 'line'
        break 
    print(line)

f.close() # it is very necesaary to close a file after you are done with it because it helps to manage memory better


g = open('Day 49 Code Test/myfile.txt', 'r') 
lines = g.readlines() # it will store all the lines of files in form of list and stores every single line as single item in list
print(lines) 
print(type(lines)) 

for i in lines:
    print(i)    # you can check that in the file after line 3 the line has not been breaked ,so line 3 didn't store \n in single line 
                # data of line 3 and not printed \n after line 3 here.if you will break the line after line 3 in file then \n will 
                # be stored in line 3 data. go and check it by breaking multiple lines and see the result
g.close()



h = open('Day 49 Code Test/myfile2.txt','w')# file opened in write mode. go and check file for results
dt = ['line 1\n', 'line 2\n', 'line 3\n'] # writelines() method does not add newline characters between the strings in the sequence
                                          # so we have add \n in each iteam of list here to break the line after printing each line
h.writelines(dt) 

dt2 = ['line 4', 'line 5', 'line 6'] 
for ln in dt2: 
    h.writelines(ln + "\n") # it is difficult to manually add \n in each iteam to break line after each line, so we will add \n
                              # for every single line stored as iteam in list by iterating the list.
h.close()