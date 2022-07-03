import matplotlib.pyplot as plt
import numpy as np
import math
import scipy
file=open("ray.dat","r")
file=file.readlines()

X=np.linspace(-2,10,50)
Y=[]
for x in X:
    l=0
    for j in file:
        if float(j)<=x:
            l+=1
    Y.append(l)

def cdf_the(x):
    if x>=0:
        return 1-np.exp(-x/2)
    elif x<0:
        return 0
    
# print([Z(x) for x in X])

# Q=scipy.vectorize(Z, otypes=[float])
plt.plot(X,Y,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()