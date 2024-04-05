import numpy as np
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stopword = stopwords.words('english')

doc1 = open('Doc1.txt').read()
doc2 = open('Doc2.txt').read()
doc3 = open('Doc3.txt').read()
doc4 = open('Doc4.txt').read()

f1 = doc1.split()
f2 = doc2.split()
f3 = doc3.split()
f4 = doc4.split()
f_doc1 = ' '.join(word for word in f1 if word.lower() not in stopword)
f_doc2 = ' '.join(word for word in f2 if word.lower() not in stopword)
f_doc3 = ' '.join(word for word in f3 if word.lower() not in stopword)
f_doc4 = ' '.join(word for word in f4 if word.lower() not in stopword)

tokens = set(f_doc1.split()) | set(f_doc2.split()) | set(f_doc3.split()) | set(f_doc4.split())
print("\n", tokens, "\n")

v1 = [1 if token in f_doc1.split() else 0 for token in tokens]
v2 = [1 if token in f_doc2.split() else 0 for token in tokens]
v3 = [1 if token in f_doc3.split() else 0 for token in tokens]
v4 = [1 if token in f_doc4.split() else 0 for token in tokens]

row_names = np.array(list(tokens))
doc_names = np.array(['Doc 1', 'Doc 2', 'Doc 3', 'Doc 4'])
incidence_matrix_data = np.array([v1, v2, v3, v4])

# Transpose the incidence matrix
transposed_matrix = incidence_matrix_data.T

# Print the header
print(f"\n\n{'':<15}", end='')
print(''.join(f"{name}\t\t" for name in doc_names))

# Print the data rows
for row_name, row_values in zip(row_names, transposed_matrix):
    print(f"{row_name:<15}", end='')
    print(''.join(f"{value}\t\t" for value in row_values))


def boolean_operation(query, row_names, transposed_matrix, doc_names):
    query_tokens = re.findall(r'\b\w+\b', query.lower())
    result_stack = []
    current_operation = None

    for token in query_tokens:
        if token == "not":
            current_operation = "not"
        elif token == "and":
            current_operation = "and"
        elif token == "or":
            current_operation = "or"
        elif token in row_names:
            token_index = np.where(row_names == token)[0][0]
            if current_operation == "not":
                result_stack[-1] = result_stack[-1] & ~transposed_matrix[token_index]
            else:
                result_stack.append(transposed_matrix[token_index])

    # Combine results using "or"
    # Combine results based on the last specified operation
    final_result = result_stack[0] if result_stack else np.ones_like(transposed_matrix[0])

    for i in range(1, len(result_stack)):
        if current_operation == "and":
            final_result = final_result & result_stack[i]
        elif current_operation == "or":
            final_result = final_result | result_stack[i]

    # Print the result
    print("\nBoolean Operation Result for Query '{}':\n".format(query))
    print(''.join(f"{name}\t\t" for name in doc_names))
    print(''.join(f"{int(value)}\t\t" for value in final_result))
    print("\nDocuments where the query is found:")
    for doc_name, value in zip(doc_names, final_result):
        if value == 1:
            print(doc_name)

# Perform boolean operation
boolean_operation('schizophrenia and not new', row_names, transposed_matrix, doc_names)