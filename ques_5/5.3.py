import matplotlib.pyplot as plt 
import numpy as np

Y=np.loadtxt("ber_gau.dat",dtype='double')

X=np.linspace(0,1,1000000)

plt.plot(X,Y,'o',marker='.',markersize=3)
# plt.xlabel("")
plt.ylabel("Y")
plt.grid()
plt.show()
