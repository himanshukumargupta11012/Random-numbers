import matplotlib.pyplot as plt
import numpy as np
import math
file=open("uni.dat","r")
file=file.readlines()
V=[]
for i in file:
    V.append(-2*math.log(1-float(i)))
# print(V)
for i in range(100):
    print(V[i])
X=np.linspace(-2,10,50)
Y=[]
for x in X:
    l=0
    for j in V:
        if j<=x:
            l+=1
    Y.append(l)

plt.plot(X,Y,'o')
plt.plot(X,Y)
plt.xlabel(x)
plt.ylabel("$F_V(x)$")
plt.grid()
plt.show()