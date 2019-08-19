# Stemming
from nltk.stem import PorterStemmer


#To tokenize text import Tokenization.py 
stemm_Token = 'Your Tokenized text'

ps = PorterStemmer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

#print (stemmed_words)

#Declare a function to return the stemmed words
def returnStemmedWords():
	return stemmed_words
