import numpy as np
import pandas as pd

x = np.array([3, 4, 6, 10, 12, 13])
y = np.array([12, 11, 15, 16, 19, 17])
num = 16

xbar = np.mean(x)
ybar = np.mean(y)

print('xbar =', xbar)
print('ybar =', ybar)

A = x - xbar
B = y - ybar
squares = (x - xbar)**2
sum = np.sum(squares)
Multi = A * B
mul_sum = np.sum(Multi)

# Create a DataFrame
df = pd.DataFrame({
    'x': x,
    'y': y,
    '(xi - xbar)': A,
    '(yi - ybar)': B,
    '(xi - xbar)^2': squares,
    'A * B': Multi
})

# Display the DataFrame
print("\nTable:")
print(df)

# Slope
m = mul_sum / sum
print("Slope m = ", m)

# Intercept
c = ybar - ((m) * xbar)
print("Intercept c = ", c)

# Predict Y
y = (m * num) + c
print("Y = ", y)
