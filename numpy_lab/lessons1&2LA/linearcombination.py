import numpy as np

v = np.array([1,0])
w = np.array([0,1])
u = np.array([0,0,0,1])

li = 5*v + -2*w
print(li)


x, y = [[1,0],[0,1]]

if len(x) == len(y):
    z = [x[i] + y[i] for i in range(len(x))]    

print(z)