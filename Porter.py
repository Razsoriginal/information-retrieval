from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "jumps", "likes", "program", "flies", "agreed"]

for w in words:
    print(w, ":", ps.stem(w))