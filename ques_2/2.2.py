import matplotlib.pyplot as plt
import numpy as np
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
Z=[]
for i in range(len(X)-1):
    Z.append((Y[i+1]-Y[i])/(X[i+1]-X[i]))

plt.plot(X,Y,'o')
plt.plot(X,Y)
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.grid()
plt.show()

plt.plot(X[0:len(X)-1],Z,'o')
plt.plot(X[0:len(X)-1],Z)
plt.xlabel("x")
plt.ylabel("$f_X(x)$")
plt.grid()
plt.show()