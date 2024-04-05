import pandas as pd
import matplotlib.pyplot as plt

# Question-1
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
tickets_sold = [2000, 2800, 3000, 2500, 2300, 2500, 1000]
plt.plot(days, tickets_sold, color='magenta', marker='o')
plt.title('Tickets Sold Each Day of the Week')
plt.xlabel('Day')
plt.ylabel('Tickets Sold')
plt.show()

# Question-2
df = pd.read_csv("clgdata.csv")
df.plot(x='College', kind='bar')
plt.title('Number of Courses Offered by Colleges in Delhi University')
plt.ylabel('Number of Courses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Question-3
df = pd.read_csv('temperature_data.csv')
df[['Min_Temperature', 'Max_Temperature']].plot(kind='hist', alpha=0.7, edgecolor='black')
plt.title('Histogram of Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

# Question-4
df = pd.read_csv('gov.csv')
colors = {'East': 'blue', 'West': 'red', 'North': 'green', 'South': 'orange'}
for region, data in df.groupby('Region'):
    if region in colors:
        plt.scatter(data['Population'], data['Literacy Rate'], s=np.sqrt(data['Literacy Rate']), label=region, c=colors[region])
plt.xlabel('Population')
plt.ylabel('Literacy Rate')
plt.legend()
plt.grid(True)
plt.show()

df = pd.read_csv('gov.csv')
average_literacy_rate = df.groupby('Region')['Literacy Rate'].mean()
plt.bar(average_literacy_rate.index, average_literacy_rate.values, color=['blue', 'green', 'red', 'orange'])
plt.title('Average Literacy Rate by Region')
plt.xlabel('Region')
plt.ylabel('Average Literacy Rate')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
