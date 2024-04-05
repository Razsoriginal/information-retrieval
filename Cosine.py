Cosine Similarity
d1=open(r"\\doc1.txt").read().lower()
d2=open(r"\\doc2.txt").read().lower()
d3=open(r"\\doc3.txt").read().lower()
d4=open(r"").read().lower()
print(d1)
print(d2)
print(d3)
print(d4)
docs=[d1,d2,d3,d4]

from nltk.corpus import stopwords
import re
sw=set(stopwords.words('english'))
for i in range(0,len(docs)):
    docs[i]=re.sub(r"[^\w\s]",'',docs[i])
    filtered_text=""
    for word in docs[i].split():
        if word.lower() not in sw:
            filtered_text+=" "+word
    docs[i]=filtered_text
    print(docs[i])

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_v=TfidfVectorizer()
tfidf_matrix=tfidf_v.fit_transform([d1,d2,d3,d4]).toarray()
print(tfidf_matrix)

import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))


for i in range(0,len(tfidf_matrix)):
    for j in range(0,len(tfidf_matrix)):
        print("Cosine Similarity between Doc",i+1,"and Doc",j+1," is "+str(cosine_similarity(tfidf_matrix[i],tfidf_matrix[j])),end="")
        if cosine_similarity(tfidf_matrix[i],tfidf_matrix[j]) > 0.70:
            print(" - Similar")
        else:
            print(" - Not Similar")