import matplotlib.pyplot as plt
import numpy as np
import math 


def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2
def cdf_the(x):
    return 1-Q(x)

A=5

def p_e_del(x):
    a=1-cdf_the(5+x)+cdf_the(-5+x)
    return a/2

delt=np.linspace(-20,20,1000)
plt.plot(delt,[p_e_del(a) for a in delt])
plt.xlabel("$delta$")
plt.ylabel("$P_e$")
plt.grid()
plt.show()