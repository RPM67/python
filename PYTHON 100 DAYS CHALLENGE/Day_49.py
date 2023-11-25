f = open("Day 49 Code Test/Day_49_test.txt",'r') # file opened in only read mode as 'r' is provided here
read = f.read() # 'read' variable stores the data from the file opened in f as a string
print(read)
f.close() # this will close the opened file in f
print(read) # this will still work here b/c data from file has been 'stored' in read variable



g = open("Day 49 Code Test/Day_49_test.txt",'w')# file opened in only write mode.new file of this name will be created if file missing
try:
    reads = g.read() # it will give you error because file is opened into write mode only.
    print(reads) 
except:
    print("can't perform other operations as file is opened into write mode only")
g.write("I am RPM the coder") # 'w' will overwrite into the opened file. go and check the file to see that the whole file has been 
                              # overwritten by the text provided in g.write(). remember, g.write() only writes into file, overwriting
                              # and appending only depends on the mode provide when file opened weather it is 'w' or 'a'
g.close()



h = open("Day 49 Code Test/Day_49_test.txt",'a') # 'a' will append into the file at the end of existing data into file.new file of 
                                                 #this name will be created if file is missing 
h.write(" I am in Day 49 of CWH Python Course. ")# 'w' will append at end of file. go check the file to see that file data has been 
                              # appended by the text provided in g.write(). remember, g.write() only writes into file, overwriting
                              # and appending only depends on the mode provide when file opened weather it is 'w' or 'a'
h.close()



with open("Day 49 Code Test/Day_49_test.txt",'r') as i:# 'with' statement closes files automatically 
    data = i.read()
    print(data)
