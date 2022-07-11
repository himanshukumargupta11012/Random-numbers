import matplotlib.pyplot as plt
import numpy as np
import math

ber=np.loadtxt('../ques_5/ber.dat',dtype='int')
gau=np.loadtxt('../ques_2/gau.dat',dtype='double')
uni=np.loadtxt('../ques_1/uni.dat',dtype='double')


gama=np.linspace(1e-10,10,50)


# ray2=[]
arr=[]
for j in range(len(gama)):
	# ray2.append([])
	arr.append([])
	for i in range(int(1e6)):
		t=math.sqrt(-gama[j]*math.log(uni[i]))
		arr[j].append(ber[i]*t+gau[i])
# ray2[j].append(math.sqrt(-gama[j]*math.log(uni[i])))

def func(gama):
	arr=[]
	for i in range(len(gau)):
		t=math.sqrt(-gama[j]*math.log(uni[i]))
		arr.append(ber[i]*t+gau[i])
	return arr
arr=np.vectorize(func)(gama)

p_e_num=[]
for i in range(len(gama)):
	l=0
	for j in range(int(1e6)):
		if (arr[i][j]>0 and ber[j]==-1) or (arr[i][j]<0 and ber[j]==1):
			l+=1
	p_e_num.append(l/1e6)

# arr3=np.vectorize(check)(gama)

def p_e_the(gama):
    return math.erfc(0)*(1-1/(math.sqrt(2/gama+1)))/2

p_e_the2=np.vectorize(p_e_the)(gama) 
    


plt.plot(gama,p_e_num,'o')
plt.plot(gama,p_e_the2)
plt.xlabel('gamma')
plt.ylabel('$P_e$')
plt.legend(['Numerical','Theoretical'])
plt.grid()
plt.show()