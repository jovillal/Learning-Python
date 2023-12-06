"""
Created on Thu Nov 27 15:11:04 2023

@author: jovillal
working with pdfs
"""
import PyPDF2

reader = PyPDF2.PdfReader(open('maxwell.pdf','rb'))  #the 'rb' means read binary
print(reader.pages)

