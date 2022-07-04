import matplotlib.pyplot as plt
import numpy as np
import math
import scipy

# file=open("ray.dat","r")
# file=file.readlines()

# X=np.linspace(-2,10,50)
# Y=[]
# for x in X:
#     l=0
#     for j in file:
#         if float(j)<=x:
#             l+=1
#     Y.append(l)


X = np.linspace(-2,15,80)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('ray.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,80):
	err_ind = np.nonzero(randvar < X[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def cdf_the(x):
    if x>=0:
        return 1-np.exp(-x/2)
    elif x<0:
        return 0

# print([Z(x) for x in X])

# Q=scipy.vectorize(Z, otypes=[float])
plt.plot(X,err,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()