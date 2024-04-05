import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

matrix_file = 'C:/Users/aakash/Videos/IR/IR/P11 29-02-2024/data.csv' 
with open(matrix_file, 'r') as file:
    reader = csv.reader(file)
    matrix = [list(map(int, row)) for row in reader]

for i in range(len(matrix[0]) + 1):
    if i == 0:
        print("-", end="\t")
    else:
        print(i, end="\t")
print()

#pip install scikit-learn


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j == 0:
            print(chr(i + 65), end="\t")
        if matrix[i][j] == 0:
            print("-", end="\t")
        else:
            print(matrix[i][j], end="\t")
    print("\n")

cosine_similarity_score = [0, ]
for i in range(len(matrix) - 1):
    vector1 = np.array(matrix[i]).reshape(1, -1)
    vector2 = np.array(matrix[i + 1]).reshape(1, -1)
    similarity_score = cosine_similarity(vector1, vector2)
    cosine_similarity_score.append(round(similarity_score.item(), 2))

css = cosine_similarity_score.copy()
max_1 = css.index(max(css))
css.pop(max_1)
max_2 = css.index(max(css))

n = 9 

predicted_rating = ((matrix[max_1][n] * cosine_similarity_score[max_1]) +
                    (matrix[max_2][n] * cosine_similarity_score[max_2])) / (
                        cosine_similarity_score[max_1] + cosine_similarity_score[max_2])
print(round(predicted_rating, 3))