import re
import numpy as np
import matplotlib.pyplot as plt

uni=open("uni.dat",'r')
uni=uni.readlines()

X=np.linspace(-3,3,100)
Y=[]
for x in X:
    l=0
    for i in uni:
        if float(i)<=x:
            l+=1
    Y.append(l)
def cdf_the(x):
    if x<0:
        return 0
    if 0<=x<1:
        return x
    if x>=1:
        return 1

Y=[i/len(uni) for i in Y]
plt.plot(X,Y,'o')
plt.plot(X,[cdf_the(x) for x in X])
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()

