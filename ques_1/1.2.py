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
Y=[i/len(uni) for i in Y]
plt.plot(X,Y,'o')
plt.plot(X,Y)
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.grid()
plt.show()