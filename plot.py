import matplotlib.pyplot as plt
import numpy as np

x=np.array([2,3,5,8,9,6,4,7,5,2,9])
y=np.array([4,5,7,1,8,4,2,1,5,3,7])

g=np.random.randint(0,100,10)
plt.plot(x,y,'H--b')
plt.plot(g,'d-.y')
plt.pie(y)
plt.title("Practice")
plt.show()
