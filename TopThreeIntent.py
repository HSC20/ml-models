import pandas as pd
import pprint
import operator
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils.validation import check_is_fitted
train_df=pd.read_csv("C:/Users/Harpreet/Desktop/JIO/check_prob.csv",encoding = "ISO-8859-1")
X = train_df['Expression']
Y = train_df['Intent']

intentList=list(Y)



def unique(list1):
     # intilize a null list
     unique_list = []

  # traverse for all elements
     for x in list1:
       # check if exists in unique_list or not
         if x not in unique_list:
             unique_list.append(x)
             # print list
     return unique_list
uniqueIntentlist=unique(intentList)
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size = 0.3, train_size = 0.7)
vectorizer = CountVectorizer()
xTrain_v = vectorizer.fit_transform(xTrain)
xTest_v = vectorizer.transform(xTest)
lr = LogisticRegression()
clf = OneVsRestClassifier(lr)
clf.fit(xTrain_v, yTrain)
 # list_ytrain=list(yTrain)
 # print(list(list_ytrain))

y_pred = clf.predict(xTest_v)
x='how are you' 
 # put("enter the expression")
y=clf.predict(vectorizer.transform(list([x])))
print(y)
z=list(clf.predict_proba(vectorizer.transform(list([x])))[0])
#
# print(z)
#
output=[]
for i,y in enumerate(z):
      output.append((i,y))
      print(output)


def Sort_Tuple(tup):
     # getting length of list of tuples
     lst = len(tup)
     for i in range(0, lst):

         for j in range(0, lst - i - 1):
             if (tup[j][1] > tup[j + 1][1]):
                 temp = tup[j]
                 tup[j] = tup[j + 1]
                 tup[j + 1] = temp
     return tup
out=Sort_Tuple(output)
print(out[-3:])
out_top_three=out[-3:]


dicString="{"
itrator=0
for i in out_top_three:
     itrator= itrator+1
     print(itrator)
     size=len(out_top_three)
     StringVar=uniqueIntentlist[i[0]]
     intentDic=StringVar + ":" + str(i[1])
     dicString=dicString + "'"+ StringVar +"'"  + ":" + str(i[1])
     if itrator == size:
         dicString =  dicString + "}"
     else :
         dicString=dicString+","

Dict = eval(dicString)
print(Dict)
sorted_d = dict( sorted(Dict.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)
