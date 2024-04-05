import pandas as pd
import numpy as np

# Reading employee data
df_emp = pd.read_csv('C:\\Users\\admin\\Downloads\\employee.csv')

# Print the records
print(df_emp)

# Extract the name and salary columns
name_sal = df_emp[['name','basic_sal']]
print(name_sal)

# Compute the total salary column
df_emp['total_sal'] = df_emp['basic_sal'] + df_emp['allowances']
print(df_emp['total_sal'])

# Find the highest basic salary
max_basic_sal = df_emp['basic_sal'].max()
print(max_basic_sal)

# Find the minimum basic salary
min_basic_sal = df_emp['basic_sal'].min()
print(min_basic_sal)

# Extract the first 5 records
first_5 = df_emp.head()
print(first_5)

# Extract the last 3 records
last_3 = df_emp.tail(3)
print(last_3)

# Creating random marks data
marks = np.random.randint(20, 101, size=(20, 3))
subjects = ['Eng', 'Phy', 'Chem']
students = ['Manoj', 'Avishkar', 'Ashay', 'Raghav', 'Ananya', 'Aarav', 'Anvit', 'Rahul', 'Vikram', 'Aishwarya', 'Aditya', 'Priya', 'Arjun', 'Meera', 'Rohan', 'Sneha', 'Kiran', 'Divya', 'Aryan', 'Neha']
df_marks = pd.DataFrame(marks, columns=subjects, index=students)
print(df_marks)

# Print complete information with the help of data frame
print(df_marks)

# Extract student name with subjects
print(df_marks.loc['Manoj'])

# Find min marks of all subjects
print(df_marks.min())

# Find max marks of all subjects
print(df_marks.max())

# Find the total marks obtained by each student by adding one column
df_marks['Total'] = df_marks.sum(axis=1)
print(df_marks)

# Extract marks of Anvit, Avishkar, Ashay
print(df_marks.loc[['Anvit','Avishkar', 'Ashay']])

# Printing alternate records
print(df_marks.iloc[::2])

# Display first 5 records
print(df_marks.head())

# Extract rows from 3 to 5
print(df_marks.iloc[2:5])

# Compute m1 = eng + phy
df_marks['m1'] = df_marks['Eng'] + df_marks['Phy']
print(df_marks)

# Compute m2 = phy + chem
df_marks['m2'] = df_marks['Phy'] + df_marks['Chem']
print(df_marks)

# Find percentage of all students
df_marks['Percentage'] = (df_marks['Total'] / 300) * 100
print(df_marks)

# Extract records if marks of eng < 70 but greater than 40
print(df_marks[(df_marks['Eng'] < 70) & (df_marks['Eng'] > 40)])

# Read rows if chem marks are between 30 and 60
print(df_marks[(df_marks['Chem'] >= 30) & (df_marks['Chem'] <= 60)])

# Calculate mean, mode, median
print("Mean:")
print(df_marks.mean())
print("Mode:")
print("EngMode:", df_marks['Eng'].mode()[0])
print("PhyMode:", df_marks['Phy'].mode()[0])
print("ChemMode:", df_marks['Chem'].mode()[0])
print("Median:")
print(df_marks.median())

# Add a column called address
df_marks['Address'] = ['Andheri', 'Bandra', 'Goregaon', 'Jogeshwari', 'Malad', 'Kandivali', 'Vile Parle', 'Dadar', 'Worli', 'Colaba', 'Chembur', 'Powai', 'Thane', 'Navi Mumbai', 'Mira Road', 'Vasai', 'Virar', 'Panvel', 'Kalyan', 'Ulhasnagar']
print(df_marks)

# Extract all students who are from Andheri
print(df_marks[df_marks['Address'] == 'Andheri'])

# Extract rows starting from 1st and then skip 1
print(df_marks.iloc[1::2])

# Print last 5 rows
print(df_marks.tail())

# Extract rows starting from 1st and then skip 2
print(df_marks.iloc[::3, ::2])

# Drop column named address
df_marks.drop('Address', axis=1, inplace=True)
print(df_marks)

# Select only those rows where eng and phy values are even
print(df_marks[(df_marks['Eng'] % 2 == 0) & (df_marks['Phy'] % 2 == 0)])