from re import T
import numpy as np
import matplotlib.pyplot as plt

file=open("tri.dat","r")
file=file.readlines()

X=np.linspace(-1,3,80)
Y=[]
for x in X:
    l=0
    for i in file:
        if float(i)<=x:
            l+=1
    Y.append(l)
Y=[i/len(file) for i in Y]

def pdf_the(x):
    if x<0:
        return 0
    if 0<=x<1:
        return x
    if 1<=x<2:
        return 2-x
    if x>=2:
        return 0

def cdf_the(x):
    if x<0:
        return 0
    if 0<=x<1:
        return x**2/2
    if 1<=x<2:
        return 2*x-x**2/2-1
    if x>=2:
        return 1

def pdf_num(i):
    return (Y[i+1]-Y[i])/(X[i+1]-X[i])

plt.plot(X,Y,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_T(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()



plt.plot(X[0:len(X)-1],[pdf_num(i) for i in range(len(X)-1) ],'o')  
plt.plot(X,[pdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$f_T(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()