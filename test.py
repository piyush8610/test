import pyttsx3
import PyPDF2
bn = input("Enter the name of the book you want to listen : ")
book = open(bn,'rb')
pdfreader = PyPDF2.PdfFileReader(book)
page = pdfreader.numPages
SP = input("Enter the starting page:")
sp1 = int(SP)
sp = sp1-1

print("no. of pages in this book are :", page)

for num in range(sp, page) :
    startingpage = pdfreader.getPage(sp)
    fulltext = startingpage.extractText()
    speaker = pyttsx3.init()
    speaker.say(fulltext)
    speaker.runAndWait()
    