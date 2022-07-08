import numpy as np
import math
from scipy import integrate
import sympy

file=np.loadtxt("ber_gau.dat",dtype='double')
file2=np.loadtxt("ber.dat",dtype='double')


l=0
for i in range(len(file)):
    if(int(file2[i])==-1 and float(file[i])>=0):
        l+=1
l=l/len(file)


m=0
for i in range(len(file)):
    if(int(file2[i])==1 and float(file[i])<0):
        m+=1
m=m/len(file)


def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2
def cdf_the(x):
    return 1-Q(x)

print("$_{e|0}_the:",cdf_the(-5))
print("p_{e|1}_the:",1-cdf_the(5))

print("$_{e|0}_num:",m)
print("p_{e|1}_num:",l)