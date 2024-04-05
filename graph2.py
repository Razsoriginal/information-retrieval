import matplotlib.pyplot as plt
import numpy as np

# Scatter plot
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)
plt.show()

# Scatter plot with multiple datasets
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y)

x = np.array([3, 4, 7, 1, 1, 8, 2, 9, 7, 3, 1, 4, 8, 4, 2])
y = np.array([105, 155, 94, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y)

plt.show()

# Scatter plot with color and colormap
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()

# Scatter plot with size
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 300, 400, 45, 500, 55, 600, 70, 80, 90, 1000])
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()

# Vertical bar chart
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.show()

# Horizontal bar chart
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
colors = ['red', 'blue', 'green', 'cyan']
plt.barh(x, y, color=colors)
plt.show()

# Vertical bar chart with specified width
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width=0.1)
plt.show()

# Horizontal bar chart with specified height
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height=0.9)
plt.show()

# Histogram
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

# Pie chart
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

# Pie chart with labels
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels)
plt.show()

# Pie chart with start angle
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# Pie chart with explode
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.2, 0, 0]
plt.pie(y, labels=mylabels, startangle=90, explode=myexplode)
plt.show()

# Pie chart with colors and legend
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["red", "blue", "black", "hotpink"]
myexplode = [0.2, 0.2, 0, 0]
plt.pie(y, labels=mylabels, colors=mycolors, explode=myexplode)
plt.legend(title="Four Fruits")
plt.show()

# Line chart
x = np.array([10, 4, 7, 2, 8]) 
y = np.array([3, 6, 9, 3, 6]) 
plt.plot(x, y)
plt.show()

# Line chart with markers, color, and size
x = np.array([10, 4, 7, 2, 8]) 
y = np.array([3, 6, 9, 3, 6]) 
plt.plot(x, y, marker='^', ms=20, mec='r') 
plt.show()

# Line chart with line style
ypoints = np.array([3, 8, 1, 10]) 
plt.plot(ypoints, ls='dotted')
plt.show()

# Line chart with different line style
ypoints = np.array([3, 8, 1, 10]) 
plt.plot(ypoints, ls='dashed')
plt.show()

# Line chart with labels and title
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) 
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) 
plt.plot(x, y) 
plt.xlabel("Average Pulse") 
plt.ylabel("Calorie Burnage") 
plt.title("Sports Watch Data")
plt.show()

# Line chart with grid
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) 
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) 
plt.plot(x, y) 
plt.xlabel("Average Pulse") 
plt.ylabel("Calorie Burnage") 
plt.title("Sports Watch Data")
plt.grid()
plt.show()

# Line chart with customized grid
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) 
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) 
plt.plot(x, y) 
plt.xlabel("Average Pulse") 
plt.ylabel("Calorie Burnage") 
plt.title("Sports Watch Data")
plt.grid(axis='x', color='green', linestyle='--', linewidth=0.5)
plt.show()