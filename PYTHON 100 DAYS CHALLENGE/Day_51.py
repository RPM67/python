with open('Day59Practice.txt','r') as f:
    print(f.read()) # here the file will be readed from starting i.e. 0th byte
    f.seek(7)   # seek has moved current position of file to 8th byte due to which the file will be readed from 8th byte i.e 8th 
                # letter and ignore the first 7 bytes of file 
    print(f.read())



with open('Day59Practice.txt','r') as f:
    print(f.tell()) # here current position of file is as defalut 0. so it will return 0 which means any operation on file like
                    # read will start from current position 0th byte
    f.seek(8)
    print(f.tell()) # here current position of file is set to 8th byte using seek() function. so it will return 8 which means any
                    # operation on file like read will start from current position 8th byte
                   


with open('file.txt','w') as f:
    f.write('abcdefghijklmn')
    f.truncate(7) # due to this truncate() fn. the file will store only till 7th byte into the file
                  # from the argument provided in write() fn.

with open('file.txt','r') as g:
    print(g.read()) # here read() fn. confirms that the file has stored only till 7th byte from 
                    # write() fn. due to truncate() fn. 