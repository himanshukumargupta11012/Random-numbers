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

# W=[]
# x=sympy.Symbol("x")
mu=0
sigma=1
# S = lambda t: np.exp(-1/2*(t-mu)**2)/(sigma*math.sqrt(2*np.pi))
# for x in X:
#     W.append(integrate.quad(S, -math.inf, x))

def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2
def cdf_the(x):
    return 1-Q(x)

plt.plot(X,Y,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.legend(["numerical", "theoretical"])
plt.grid()
plt.show()

def pdf_the(x):
    return np.exp(-1/2*(x-mu)**2)/(sigma*math.sqrt(2*np.pi))


def pdf_num(i):
    return (Y[i+1]-Y[i])/(X[i+1]-X[i])

plt.plot(X[0:len(X)-1],[pdf_num(i) for i in range(len(X)-1)],'o')
plt.plot(X,[pdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$f_X(x)$")
plt.legend(["numerical","theoretical"])
plt.grid()
plt.show()