# Linear Regression for 2 arrays
import matplotlib.pyplot as plt
from scipy import stats

#df = pd.read_csv("Emp Sal - Sheet1.csv")
#x = df['Emp']
#y = df['Sal']

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x,y) # Will give us the value of m and b, the 'r' is used to determin

def myfunc(x):
    return slope*x+intercept

mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()
# print(mymodel) also which code is this
