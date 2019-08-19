from nltk import pos_tag


#Stopword filteration stemming  are suggested before this step, Import text from Stemming.py/StopwordFilterations.py
Tokenized_words = 'Tokenized Text'
#Identify POS
tokens_pos = pos_tag(stemmed_words)
a = [tokens_pos]

# Function to extract two pattern tags                
def match2(token_pos,pos1,pos2):
    for subsen in token_pos:
        # avoid index error and catch last three elements
        end = len(subsen) - 1
        for ind, (a, b) in enumerate(subsen, 1):
            if ind == end:
                break
            if b == pos1 and subsen[ind][1] == pos2:
                yield ("{} {}".format(a, subsen[ind][0], subsen[ind + 1][0]))

#Rule based extraction - Verb/Noun followed by Numeral, Customize the rules as required.
print ('***** - Text Analytics Results - *****')
print(list(match2(a,'VB','JJ')))
print(list(match2(a,'JJR','JJ')))
print(list(match2(a,'NN','JJ')))
print(list(match2(a,'VB','CD')))
print(list(match2(a,'JJR','CD')))
print(list(match2(a,'NN','CD')))
print(list(match2(a,'VBG','CD')))

