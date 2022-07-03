import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import sympy
import math
gau=open("gau.dat","r")
gau=gau.readlines()
X=np.linspace(-5,5,100)
Y=[]
for x in X:
    l=0
    for i in gau:
        if float(i)<=x:
            l+=1
    Y.append(l)
Y=[i/len(gau) for i in Y]
W=[]
x=sympy.Symbol("x")
mu=0
sigma=1

S = lambda t: np.exp(-1/2*(t-mu)**2)/(sigma*math.sqrt(2*np.pi))
for x in X:
    W.append(integrate.quad(S, -math.inf, x))


plt.plot(X,Y,'o')
plt.plot(X,W)
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.legend(["numerical", "theoretical"])
plt.grid()
plt.show()

A=[]
Z=[]
for i in range(len(X)-1):
    Z.append((Y[i+1]-Y[i])/(X[i+1]-X[i]))
for x in X:
    A.append(np.exp(-1/2*(x-mu)**2)/(sigma*math.sqrt(2*np.pi)))
plt.plot(X[0:len(X)-1],Z,'o')
plt.plot(X,A)
plt.xlabel("x")
plt.ylabel("$f_X(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()