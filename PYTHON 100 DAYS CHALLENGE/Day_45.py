import rpm 
# above a critical fn. 'test' is running in rpm.py file and we want to import some of the other functions from that module or file in
# this Day_45.py file. 
# By importing that module dirctly without checking will run all the functions including that critical fn 'test' also if the functions  
# are running directly in that module into this Day_45.py file which may harm our system. 

# so we should check that module that weather any fn. written in that module is running directly or indirectly.
# if the function written in that module is running directly in that file then those fn. will run in this file too where that module
# is imported. 'if the function written in that module is written inside __name__ == "__main__" then that function will run only 
# when that file is run directly and will not run in this file where that module is only imported.' however if we want to run the
# functions of that file in this file we can do it.

__name__ == "__main__"
# This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script,
# without running the code in the original script.


