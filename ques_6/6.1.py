import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import math
# file=open("gau_gau.dat","r")
# file=file.readlines()
# x=sy.Symbol('x')
# X=np.linspace(-1,17,80)
# Y=[]
# for x in X:
#     l=0
#     for i in file:
#         if float(i)<=x:
#             l+=1
#     Y.append(l)

X = np.linspace(-1,17,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('gau_gau.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < X[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

a=1/2
def cdf_the(x):

    if x<0:
        return 1e-5
    if x>=0:
        return 1-np.exp(-1*a*x)

def pdf_the(x):
    if x<0:
        return 0
    else:
        return a*np.exp(-1*a*x)


def pdf_num(i):
    return (err[i+1]-err[i])/(X[i+1]-X[i])

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