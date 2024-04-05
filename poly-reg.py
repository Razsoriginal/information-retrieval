import matplotlib.pyplot as plt
import numpy

#df = pd.read_csv("Emp Sal - Sheet1.csv")
#x = df['Emp']
#y = df['Sal']

x = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100,98,99,101,102,105,80,98,99,101,101]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 4)) # 3 is the degree of the slope
myline = numpy.linspace(1, 30) # 21 is the length of the line i.e. no. of points covering

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

speed = mymodel(10)
print(speed)
