# Usage: Extract the paragraph from the PDF
import sys
#If PyPDF2 package not installed, then first install it
#pip install PyPDF2
import PyPDF2
#Note: Replace back-slash character on windows '\' with forward slash '/'
mypdfpath = 'Your PDF File'

#Open PDF object
pdfFileObj = open(mypdfpath, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageText = ''

#Read a range of pages and looping through all the pages   
number_of_pages = pdfReader.getNumPages()
#print (number_of_pages)
for page_number in range(number_of_pages):   # use xrange in Py2
        page = pdfReader.getPage(page_number)
        page_content = page.extractText()
        pageText = pageText + ' ' + page_content
		
#Remove new lines and merge the words into one string
pageText = pageText.replace("\n",'')

#Paragraph Extraction from defined reference points in PDF
def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

#Start : Check of reference points for paragraph extraction
desired = between(pageText, 'Reference Point Start', 'Reference Point End')

#Replace degree underscore with degree characters


#Declare a function to return the paragraph value
def returnParagraph():
	return desired