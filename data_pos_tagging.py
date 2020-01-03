import pandas as pd
import csv
from nltk import  pos_tag_sents
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
df = pd.read_csv("C:/Users/Harpreet/Desktop/jio/exp.csv",encoding = "ISO-8859-1" )
x=df['Expression']
tagged_texts = pos_tag_sents(map(word_tokenize, x))
#print(tagged_texts)
a=[]
for i in tagged_texts:
    for j in i:
        print(j)
        a.append(j)
data=pd.DataFrame(a, columns =['sentence','word', 'Tag'])
#print(data)
data.to_csv('file1.csv')

