import nltk
import re
from nltk.corpus import stopwords
from nltk.probability import FreqDist
 
def remove_StopWords(doc):
    swords = set(stopwords.words('english'))
    with open(doc, 'r', encoding='utf-8') as file:
        data = file.read()
    words = re.sub(r'[^a-zA-Z\s]', '', data).split()
    ans = ""
    for w in words:
        if w.lower() not in swords:
            ans += w + " "
    return ans
 
def get_word_frequency(doc, word):
    with open(doc, 'r', encoding="utf-8") as file:
        data = file.read()
    words = re.sub(r'[^a-zA-Z\s]', '', data).split()
    fdist = FreqDist(words)
    return str(fdist[word])

doc_1 = "C:/Users/aakash/Videos/IR/IR/Similairty_cosine/para1.txt"
doc_2 = "C:/Users/aakash/Videos/IR/IR/Similairty_cosine/para2.txt"
doc_3 = "C:/Users/aakash/Videos/IR/IR/Similairty_cosine/para3.txt"

ans1 = remove_StopWords(doc_1)
ans2 = remove_StopWords(doc_2)
ans3 = remove_StopWords(doc_3)
 
main = list(set(ans1.split() + ans2.split() + ans3.split()))

# Print header
print(f"{'Word': <10} {'Document 1': <10} {'Document 2': <10} {'Document 3': <10}")

# Print word frequencies
for w in main:
    print(f"{w : <10}", end="")
    print(f"{get_word_frequency(doc_1, w) : <10}", end="")
    print(f"{get_word_frequency(doc_2, w) : <10}", end="")
    print(f"{get_word_frequency(doc_3, w) : <10}")