import re
from nltk.corpus import stopwords

#load NLTK stopwords
stop_words = set(stopwords.words('english'))

#Read the contents of file
with open('C:/Users/aakash/Videos/IR/stopwords.txt',"r") as file:
    data = file.read()

#removing punctuation4
cleaned_data = re.sub(r'[^\w\s]','',data)

#Tokenize the cleaned data
words = cleaned_data.split()

#fliter out stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]
 
result = ' '.join(filtered_words)
print(result)