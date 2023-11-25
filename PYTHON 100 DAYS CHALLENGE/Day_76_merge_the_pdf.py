#  pip install pyPDF2 to install pyPDF2 module that helps in merging the pdf files together
from PyPDF2 import PdfWriter
import os 

merger = PdfWriter()

pdf_files = [file for file in os.listdir() if file.endswith(".pdf")] # it stores all the pdf files from this current directory

for pdf in pdf_files:
    merger.append(pdf) # it attaches or appends the 1st pdf file in list pdf_files with all the next stored pdf files from list 
    
merger.write("merged-pdf.pdf") # it writes all the contents of the merged pdf file into a new pdf file
merger.close()