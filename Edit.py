def levenshteinRecursive(str1, str2, m, n, memo):
    # Check if the value is already computed
    if memo[m][n] != -1:
        return memo[m][n]
    
    # Base cases
    if m == 0:
        memo[m][n] = n
        return n
    if n == 0:
        memo[m][n] = m
        return m
      
    # If characters at the current position are equal
    if str1[m - 1] == str2[n - 1]:
        memo[m][n] = levenshteinRecursive(str1, str2, m - 1, n - 1, memo)
        return memo[m][n]
    
    # If characters at the current position are different
    memo[m][n] = 1 + min(
        levenshteinRecursive(str1, str2, m, n - 1, memo),         # Insert
        levenshteinRecursive(str1, str2, m - 1, n, memo),         # Remove
        levenshteinRecursive(str1, str2, m - 1, n - 1, memo)      # Replace
    )
    return memo[m][n]
 
# Function to initialize memoization matrix with -1
def initializeMemo(m, n):
    return [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

# Driver code
str1 = "kitten"
str2 = "sitting"
m, n = len(str1), len(str2)
memo = initializeMemo(m, n)
distance = levenshteinRecursive(str1, str2, m, n, memo)

# Print Levenshtein distance
print("Levenshtein Distance:", distance)

# Print the memoization matrix
print("Memoization Matrix:")
for row in memo:
    print(row)