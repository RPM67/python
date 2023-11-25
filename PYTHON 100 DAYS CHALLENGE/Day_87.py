import shutil

shutil.copy("Day_87.py","Day_87_copy.py") # it will copy the file 'Day_87.py' with its content into the new file 'Day_87_copy.py' by
                                          # creating that file itself. if file already exist then it will overwrite that file

shutil.copy2("Day_87.py","Day_87_copy.py") # This function is similar to shutil.copy, but it also preserves more metadata about the 
                                           # original file, such as the timestamp.
                                           
shutil.copytree("practice_set","practice_set_copy")  # This function copies the directory 'practice_set' into a new directory 
                                                     # 'practice_set_copy'. If the destination location already exists, the existing 
                                                     # directory will be merged with it.   
                            
shutil.move("encrypted.txt","practice_set") # This function moves the file 'encrypted.txt' to a folder practice_set       

shutil.rmtree("practice_set_copy") # This function deletes the directory 'practice_set_copy', along with all of its contents                           
                                         