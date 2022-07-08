import matplotlib.pyplot as plt 
import math
import numpy as np

A=np.linspace(0,10,50)

def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2
def cdf_the(x):
    return 1-Q(x)

def p_e(x):
    a=(cdf_the(-x)-cdf_the(x))/2+1/2
    return a

def p_e_num(X):
    B=[]
    for i in range(len(X)):
        B.append((cdf_num(-X)[i]-cdf_num(X)[i])/2+1/2)
    return B
    
def cdf_num(A):
    simlen = int(1e6)
    err = []
    #randvar = np.random.normal(0,1,simlen)
    randvar = np.loadtxt('../ques_2/gau.dat',dtype='double')
    for i in range(np.size(A)):
	    err_ind = np.nonzero(randvar < A[i]) 
	    err_n = np.size(err_ind)
	    err.append(err_n/simlen) 
    return err



plt.plot(A,p_e_num(A),'o')
plt.plot(A,[p_e(a) for a in A])
plt.xlabel("A")
plt.ylabel("$P_e$")
plt.grid()
plt.show()