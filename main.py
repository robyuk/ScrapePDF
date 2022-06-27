# Install the PyMuPDF library
import fitz

with fitz.open("students.pdf") as pdf:
  
  firstpage=pdf[0].get_text()  #get the first page text

  allpages=''
  for page in pdf:
    print(20*'-')
    print(page.get_text())
    allpages=allpages+page.get_text() #get text from all pages