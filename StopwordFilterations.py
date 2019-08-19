# Usage: Remove the stopwords from paragraph/tokens.

# Define an array of comments to test.
import nltk


from nltk.corpus import stopwords

#Retrieving tokens from Tokenization 
#To Tokenize your desired text, import Tokenization.py 
tokens = 'Tokenized Text'

#Stopwords
stop_words=set(stopwords.words("english"))

tokenized_sent = tokens

#Removing Stopwords from tokens
filtered_sent=[]
for w in tokenized_sent:
		if w not in stop_words:
			filtered_sent.append(w)
	
#print("Filterd Sentence, After Stop words:",filtered_sent)

#Declare a function to return the filtered sentence by removing the stopwords
def returnFilteredText():
	return filtered_sent

