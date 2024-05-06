f=open("podaci005.txt", "r")
noc=int(f.readline()) # broj centara
nopt=int(f.readline()) # broj tocaka
dimpt=int(f.readline()) # dimenzija tocaka


import sklearn
from sklearn.cluster import KMeans


nv=[]
for i in range(10000):
	a=f.readline()
	x=a.split()
	nv.append(x)


m=len(nv[0])
for i in range(10000):
	for j in range(m):
		nv[i][j]=float(nv[i][j])


wcss=[]
for i in range(20, 31):
	kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
	kmeans.fit(nv)
	wcss.append(kmeans.inertia_)

wcss


f.close()
x=[]
for i in range(20, 31):
	x.append(i)


x


from scipy import stats

y=x[:]
for i in range(11):
	y[i]=wcss[i]*x[i]*x[i]


y

lr = stats.linregress(x,y)


a = lr.intercept
b = lr.slope


e=[]
for i in range(11):
	va=a/(x[i]*x[i])+ b/x[i] 
	e.append(va)

e

nocl = []
for i in range(11):
	nocl.append(wcss[i]-e[i])

nocl

k = 0
mini = nocl[0]
for i in range(1, 11):
    if nocl[i] < mini:
        mini = nocl[i]
        k = i
print(x[k])
print(mini)

x 

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.plot(x,wcss)
plt.draw()
plt.show()

