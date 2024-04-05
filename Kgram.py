with open("C:/Users/aakash/Videos/IR/IR/P3 18-12-2023/kgram.txt", "r") as file:
    data = file.read()

# Add '$' at the beginning and end of the text
data = '$' + data.strip() + '$'

# Add '$' at whitespace between words
data = data.replace(' ', '$')

k = int(input("Enter k: "))
kgram = []
for i in range(0, len(data) - k + 1):
    kgram.append(data[i:i+k])

print(kgram)