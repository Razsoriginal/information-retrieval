import io
 import pandas as pd
 import numpy as np
 from sklearn.tree import DecisionTreeClassifier
 from sklearn.model_selection import train_test_split
 from sklearn import metrics
 from sklearn.tree import export_graphviz
 from io import StringIO
 from IPython.display import Image
 import pydotplus
 import matplotlib.pyplot as plt
 import matplotlib.image as mpimg

 df=pd.read_csv('d.csv')
 print(df)
 features = list(df.columns[1:5])
 target = df.columns[5]
 y = df[target]
 x = df[features]
 # print(x)
 # print(y)
 clf = DecisionTreeClassifier(criterion = "entropy", max_depth = 4, max_features=3)
 clf = clf.fit(x, y)
 dot_data = StringIO()
 export_graphviz(clf, out_file = dot_data, filled = True,
 rounded = True, special_characters = True, feature_names = features, class_names = ["strep", "cold","aller"])
 graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
 graph.write_png("temp.png")
 img=mpimg.imread('temp.png')
 imgplot = plt.imshow(img)
 plt.show()


from sklearn import tree
clf = tree.DecisionTreeClassifier()
#[height, hair-length, voice-pitch]
X = [ [180, 15,0],
[167, 42,1],
[136, 35,1],
[174, 15,0],
[141, 28,1],
[153,40,0]]
Y = ['man', 'woman', 'woman', 'man', 'woman', 'man']
clf = clf.fit(X, Y)
prediction = clf.predict([[160, 50,1]])
print(prediction)
