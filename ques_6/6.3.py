import matplotlib.pyplot as plt
import numpy as np
import math 

X=np.linspace(-1,6,80)

randvar = np.loadtxt('gau_gau2.dat',dtype='double')

simlen = int(1e6)
Y = []
#randvar = np.random.normal(0,1,simlen)

for i in range(len(X)):
	err_ind = np.nonzero([math.sqrt(x) for x in randvar] < X[i]) 
	err_n = np.size(err_ind) 
	Y.append(err_n/simlen)

def pdf(i):
    return (Y[i+1]-Y[i])/(X[i+1]-X[i])

def pdf_the(x):
    if x<0:
        return 0
    if x>=0:
        return math.exp(-x**2/2)*x

def cdf_the(x):
    if x<0:
        return 0
    if x>=0:
        return 1-math.exp(-x**2/2)

plt.plot(X,Y,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_A(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()


plt.plot(X[0:len(X)-1],[pdf(i) for i in range(len(X)-1) ],'o')
plt.plot(X,[pdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$f_A(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()