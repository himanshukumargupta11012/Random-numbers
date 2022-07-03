import numpy as np
import matplotlib.pyplot as plt

file=open("gau_gau.dat","r")
file=file.readlines()

X=np.linspace(-1,17,80)
Y=[]
for x in X:
    l=0
    for i in file:
        if float(i)<=x:
            l+=1
    Y.append(l)

def pdf(i):
    return (Y[i+1]-Y[i])/(X[i+1]-X[i])

plt.plot(X,Y,'o')
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()



plt.plot(X[0:len(X)-1],[pdf(i) for i in range(len(X)-1) ],'o')
plt.xlabel("x")
plt.ylabel("$f_V(x)$")
plt.grid()
plt.legend(["numerical","theoretical"])
plt.show()