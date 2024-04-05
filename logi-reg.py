import numpy
from sklearn import linear_model

X = numpy.array([300,204,209,144,172,165,492,437,496,452,369,588,105,208,300]).reshape(-1,1)
y = numpy.array([0,0,0,0,0,0,1,1,1,1,1,1,1,0,0])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

predicted = logr.predict(numpy.array([500]).reshape(-1,1))
print(predicted)


import numpy
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('winequalityN.csv')
df = df.head(20)

qual = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1, 9:1, 10:1}
df = df.dropna()
df = df.head(25)
df["quality"] = df["quality"].map(qual)

x = df.drop(['type', 'quality'], axis=1)
y = df['quality']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.12)

Lreg = LogisticRegression()
Lreg.fit(x_train, y_train)

yprediction = Lreg.predict(x_test)
train_acc = Lreg.score(x_test, y_test)
print("The Accuracy for Testing Set is {}".format(train_acc * 100))

df2 = pd.DataFrame(x_test)
df2["quality"] = yprediction
print("Predicted Dataset: \n", df2)


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

col_names = ['preg', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
df = pd.read_csv('diabetes.csv', header=None, names=col_names)
df = df.iloc[1:]
fe_cols = ['preg', 'glucose', 'bp', 'insulin', 'bmi', 'pedigree', 'age']
x = df[fe_cols].astype(float)
y = df['label'].astype(int)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.57)

Lreg = LogisticRegression()
Lreg.fit(x_train, y_train)

yprediction = Lreg.predict(x_test)
train_acc = Lreg.score(x_test, y_test)
print("The Accuracy for Testing Set is {:.2f}%".format(train_acc * 100))

df2 = pd.DataFrame(x_test)
df2["diabetes"] = yprediction
print("Predicted Dataset: \n", df2)
