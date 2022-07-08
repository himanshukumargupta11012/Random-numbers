import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import math

X = np.linspace(-1,17,100)
simlen = int(1e6)
err = []
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('gau_gau.dat',dtype='double')

for i in range(0,100):
	err_ind = np.nonzero(randvar < X[i]) 
	err_n = np.size(err_ind)
	err.append(err_n/simlen) 

def pdf_num(i):
    return (err[i+1]-err[i])/(X[i+1]-X[i])

def cdf_the(x):

    if x<0:
        return 0
    if x>=0:
        return 1-np.exp(-x/2)

def pdf_the(x):
    if x<0:
        return 0
    else:
        return np.exp(-x/2)/2


plt.plot(X,err,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()



plt.plot(X[0:len(X)-1],[pdf_num(i) for i in range(len(X)-1) ],'o')
plt.plot(X,[pdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$f_V(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()