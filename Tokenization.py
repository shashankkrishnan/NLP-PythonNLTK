# Usage: Segregate each word in the paragraph as tokens.

# Define an array of comments to test.
import nltk

from nltk import word_tokenize
#Retrieving paragraph from ParagraphExtraction 
comment = 'Your Text'
comment = [comment.replace("\n",'')]

# Generate list of tokens
for i in range(0,1):
    tokens = word_tokenize(comment[i]) 
#print ("Tokens - ", tokens)

#Declare a function to return the tokens value
def returnTokens():
	return tokens