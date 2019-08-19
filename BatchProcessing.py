import os
import sys
	#If PyPDF2 package not installed, then first install it
	#pip install PyPDF2
import PyPDF2
import nltk
import Tokenization
from nltk.stem import PorterStemmer


from nltk import word_tokenize
from nltk.corpus import stopwords

path = 'D:/Work/NLP/Docs/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for f in files:
    # Usage: Extract the paragraph from the PDF
	
	#Note: Replace back-slash character on windows '\' with forward slash '/'
	mypdfpath = f

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
#######################################################################
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
	desired = between(pageText, 'Heat Treatment', 'MATERIAL REQUIREMENTS')

	#Replace degree underscore with degree characters
	desired = desired.replace('º','°')
	print (desired)
########################################################################
     #Tokenization
comment = desired
comment = [comment.replace("\n",'')]

# Generate list of tokens
for i in range(0,1):
    tokens = word_tokenize(comment[i]) 
#print ("Tokens - ", tokens)

#########################################################################
	# Stopword Filertaion



#Stopwords
stop_words=set(stopwords.words("english"))

tokenized_sent = tokens

#Removing Stopwords from tokens
filtered_sent=[]
for w in tokenized_sent:
		if w not in stop_words:
			filtered_sent.append(w)
	
#print("Filterd Sentence, After Stop words:",filtered_sent)
############################################################################
     #Stemming


	
	

