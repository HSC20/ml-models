import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
train_df=pd.read_csv("C:/Users/Harpreet/Desktop/JIO/exp.csv",encoding = "ISO-8859-1")
X = train_df['Expression']
Y = train_df['Intent']
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size = 0.3, train_size = 0.7)
vectorizer = CountVectorizer()
xTrain_v = vectorizer.fit_transform(xTrain)
xTest_v = vectorizer.transform(xTest)
lr = LogisticRegression()
clf = OneVsRestClassifier(lr)
clf.fit(xTrain_v, yTrain)
y_pred = clf.predict(xTest_v)
x=input("enter the expression")
print(clf.predict(vectorizer.transform(list([x]))))
