import time
# time.time()
print(time.time()) # it will return the time that has been passed from epoch(the point in time around 1970 when the time module was 
                   # intialised) till now in seconds as floating point number

t1 = time.time() # t1 will store the time in seconds that has been passed from epoch till now when this specific line of code has 
                 # been executed. 
for i in range(50000):
    print(i)
t2 = time.time() # t2 will store the time in seconds that has been passed from epoch till now when this specific line of code has 
                 # been executed.

print()
print(t1) # it will print the time stored in t1 in second that has been passed from epoch till the execution of line t1 which is 
          # before the execution of for loop
print(t2) # it will print the time stored in t2 in second that has been passed from epoch till the execution of line t2 which is 
          # after the execution of for loop

print(t2-t1) # t1 variable will store the time passed from epoch to till the execution of line t1 which is before execution of for 
             # loop and t2 variable will store the time passed from epoch to till the execution of line t2 which is after execution
             # of for loop. now since we are printing a big range of numbers using the for loop after storing time before execution
             # of for loop in t1, so it is obvious that the for loop will take some time to print the numbers. so t2-t1 will
             # print the difference of time stored after execution of for loop and before execution of for loop which will also be
             # equal to time taken by for loop to print the numbers from 1 to 50000. 


# time.sleep()
print("start time : ",time.time())
time.sleep(5) # it will stop the execution of rest of the program where it is encountered for given seconds 
print("end time : ",time.time())

t = time.localtime() 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t) 
print(formatted_time) # the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a 
                      # specified format. The format string contains codes that represent different parts of the time value, such as 
                      # the year, the month, the day, the hour, the minute, and the second.


